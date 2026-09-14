import type {
  Check,
  CheckResult,
  Checkpoint,
  Variables,
  Target,
} from "../shared/lab.js";
import { interpolate } from "../shared/lab.js";

export interface Evidence {
  resource(target: Target): Promise<any | null>;
  diagnostic(path: string): Promise<unknown>;
}
const field = (object: any, path: string): unknown =>
  path
    .split(".")
    .reduce(
      (o, key) => (o != null && Object.hasOwn(o, key) ? o[key] : undefined),
      object,
    );
const stablePod = (p: any) => ({
  uid: p?.metadata?.uid,
  name: p?.metadata?.name,
  namespace: p?.metadata?.namespace,
  node: p?.spec?.nodeName ?? null,
  phase: p?.status?.phase,
  containers: p?.spec?.containers?.map((c: any) => ({
    name: c.name,
    image: c.image,
  })),
});
const same = (a: unknown, b: unknown) =>
  JSON.stringify(a) === JSON.stringify(b);
export async function validate(
  checks: Check[],
  evidence: Evidence,
  vars: Variables,
  checkpoints: Record<string, Checkpoint>,
): Promise<CheckResult[]> {
  const cache = new Map<string, Promise<any>>();
  const get = (target: Target) => {
    const key = JSON.stringify(target);
    if (!cache.has(key)) cache.set(key, evidence.resource(target));
    return cache.get(key)!;
  };
  return Promise.all(
    checks.map(async (check) => {
      let expected: unknown = true,
        observed: unknown = null;
      try {
        if (check.type === "diagnostic") {
          let doc: any;
          try {
            doc = await evidence.diagnostic(check.path);
          } catch (error) {
            return {
              id: check.id,
              label: check.label,
              status: "unmet" as const,
              expected: "A valid diagnostic JSON file",
              observed: (error as Error).message,
            };
          }
          if (check.source === "pod") {
            const live = await get({
              resource: "pod",
              name: "nginx",
              namespace: "default",
            });
            expected = live ? stablePod(live) : "The live default/nginx Pod";
            observed = stablePod(doc);
            if (!live || doc?.kind !== "Pod" || !doc?.metadata?.uid)
              throw new RequirementError(
                "Save the current Pod as JSON, including its metadata, spec, and status.",
              );
          } else {
            const live = await get({
              resource: "pods",
              namespace: "kube-system",
            });
            if (!live || !Array.isArray(live.items))
              throw new Error("Invalid Kubernetes PodList response");
            if (
              !Array.isArray(doc?.items) ||
              !["List", "PodList"].includes(doc.kind)
            )
              throw new RequirementError(
                "Save the kube-system Pod list as JSON.",
              );
            const components = [
              "kube-apiserver",
              "kube-controller-manager",
              "etcd",
              "kube-proxy",
            ];
            const projection = (items: any[]) =>
              items
                .filter(
                  (p) =>
                    components.includes(p?.metadata?.labels?.component) ||
                    p?.metadata?.labels?.["k8s-app"] === "kube-proxy",
                )
                .map((p) => ({ name: p.metadata.name, uid: p.metadata.uid }))
                .sort((a, b) => a.name.localeCompare(b.name));
            for (const component of components)
              if (
                !live.items.some(
                  (p: any) =>
                    p.metadata?.labels?.component === component ||
                    p.metadata?.labels?.["k8s-app"] === component,
                )
              )
                throw new Error(
                  `Lab control-plane inventory is missing ${component}`,
                );
            if (
              live.items.some(
                (p: any) => p.metadata?.labels?.component === "kube-scheduler",
              )
            )
              throw new Error("Scheduler is unexpectedly running");
            expected = projection(live.items);
            observed = projection(doc.items);
            if (
              doc.items.some(
                (p: any) =>
                  p.metadata?.labels?.component === "kube-scheduler" ||
                  p.metadata?.name?.startsWith("kube-scheduler-"),
              )
            )
              throw new RequirementError(
                "The saved inventory still contains a scheduler Pod.",
              );
            if (
              doc.items.some(
                (p: any) => p?.metadata?.namespace !== "kube-system",
              )
            )
              throw new RequirementError(
                "Save only the kube-system namespace inventory.",
              );
          }
        } else {
          const object = await get(check.target);
          if (check.type === "exists") {
            expected = true;
            observed = object !== null;
          } else if (!object) {
            expected = "Resource exists";
            observed = "Resource not found";
          } else if (check.type === "field") {
            expected =
              typeof check.equals === "string"
                ? interpolate(check.equals, vars)
                : check.equals;
            observed = field(object, check.path) ?? null;
          } else if (check.type === "condition") {
            expected = check.equals;
            observed =
              object.status?.conditions?.find(
                (c: any) => c.type === check.condition,
              )?.status ?? null;
          } else if (check.type === "container") {
            expected = {
              name: check.name,
              image: interpolate(check.image, vars),
            };
            const c = object.spec?.containers?.find(
              (c: any) => c.name === check.name,
            );
            observed = c ? { name: c.name, image: c.image } : null;
          } else if (check.type === "uidChanged") {
            const previous = checkpoints[check.checkpoint]?.podUID;
            expected = `A new UID after ${check.checkpoint}`;
            observed = object.metadata?.uid ?? null;
            const passed = !!previous && !!observed && observed !== previous;
            return {
              id: check.id,
              label: check.label,
              status: passed ? ("passed" as const) : ("unmet" as const),
              expected,
              observed,
            };
          }
        }
        return {
          id: check.id,
          label: check.label,
          status: same(expected, observed) ? "passed" : "unmet",
          expected,
          observed,
        };
      } catch (error) {
        return {
          id: check.id,
          label: check.label,
          status: error instanceof RequirementError ? "unmet" : "error",
          expected,
          observed,
          message: (error as Error).message,
        };
      }
    }),
  );
}
class RequirementError extends Error {}
