import { z } from "zod";

const filePath = z
  .string()
  .regex(/^[a-zA-Z0-9_/-]+\.(md|yaml|json)$/)
  .refine(
    (p) => !p.split("/").includes("..") && !p.startsWith("/"),
    "Must be a relative lab path",
  );
const resource = z
  .object({
    resource: z.enum(["pod", "pods", "namespace", "nodes"]),
    name: z
      .string()
      .regex(/^[a-z0-9.-]+$/)
      .optional(),
    namespace: z
      .string()
      .regex(/^[a-z0-9-]+$/)
      .default("default"),
  })
  .strict();
const base = { id: z.string().regex(/^[a-z0-9-]+$/), label: z.string().min(1) };
const value = z.union([z.string(), z.number(), z.boolean(), z.null()]);
export const checkSchema = z.discriminatedUnion("type", [
  z.object({ ...base, type: z.literal("exists"), target: resource }).strict(),
  z
    .object({
      ...base,
      type: z.literal("field"),
      target: resource,
      path: z.string().regex(/^[a-zA-Z0-9_.]+$/),
      equals: value,
    })
    .strict(),
  z
    .object({
      ...base,
      type: z.literal("condition"),
      target: resource,
      condition: z.string(),
      equals: z.string(),
    })
    .strict(),
  z
    .object({
      ...base,
      type: z.literal("container"),
      target: resource,
      name: z.string(),
      image: z.string(),
    })
    .strict(),
  z
    .object({
      ...base,
      type: z.literal("uidChanged"),
      target: resource,
      checkpoint: z.string(),
    })
    .strict(),
  z
    .object({
      ...base,
      type: z.literal("diagnostic"),
      path: filePath,
      source: z.enum(["pod", "systemPods"]),
    })
    .strict(),
]);
export const labSchema = z
  .object({
    schemaVersion: z.literal(1),
    id: z.string().regex(/^[a-z0-9-]+$/),
    version: z.string(),
    title: z.string(),
    description: z.string(),
    runtime: z
      .object({
        kubernetesVersion: z.string().regex(/^v\d+\.\d+\.\d+$/),
        nginxImage: z.string().regex(/^nginx@sha256:[a-f0-9]{64}$/),
        toolboxImage: z.literal("kubernetes-lab-toolbox:0.1.0"),
        nodes: z.literal(2),
        setup: z.literal("manual-scheduling"),
      })
      .strict(),
    steps: z
      .array(
        z
          .object({
            id: z.string().regex(/^[a-z0-9-]+$/),
            title: z.string(),
            instructions: filePath,
            hint: z.string(),
            checks: z.array(checkSchema).min(1),
          })
          .strict(),
      )
      .min(1),
  })
  .strict()
  .superRefine((lab, ctx) => {
    const ids = new Set<string>();
    for (const [index, step] of lab.steps.entries()) {
      if (ids.has(step.id))
        ctx.addIssue({
          code: "custom",
          message: "Duplicate step ID",
          path: ["steps", index],
        });
      const checks = new Set<string>();
      for (const check of step.checks) {
        if (checks.has(check.id))
          ctx.addIssue({
            code: "custom",
            message: "Duplicate check ID",
            path: ["steps", index],
          });
        checks.add(check.id);
        if (check.type === "uidChanged" && !ids.has(check.checkpoint))
          ctx.addIssue({
            code: "custom",
            message: "UID comparison must reference a previous step",
            path: ["steps", index],
          });
      }
      ids.add(step.id);
    }
  });
export type Lab = z.infer<typeof labSchema>;
export type Check = z.infer<typeof checkSchema>;
export type Target = z.infer<typeof resource>;
export type CheckResult = {
  id: string;
  label: string;
  status: "passed" | "unmet" | "error";
  expected: unknown;
  observed: unknown;
  message?: string;
};
export type Checkpoint = {
  passedAt: string;
  podUID: string;
  results: CheckResult[];
};
export type Progress = {
  current: number;
  checkpoints: Record<string, Checkpoint>;
};
export type Variables = {
  worker: string;
  controlPlane: string;
  nginxImage: string;
};
export const interpolate = (text: string, vars: Variables) =>
  text.replace(
    /\{\{(worker|controlPlane|nginxImage)\}\}/g,
    (_, key: keyof Variables) => vars[key],
  );
