import { z } from "zod";
import { labSchema, checkSchema } from "./lab.js";

export const idSchema = z.string().regex(/^[a-z0-9-]+$/).max(100);
export const starterPathSchema = z.string().max(240)
  .regex(/^[a-zA-Z0-9_-]+(?:\/[a-zA-Z0-9_-]+)*\.(?:yaml|yml|json|md|txt)$/);
const text = z.string().max(2_000_000);
export const documentSchema = z.object({
  definition: z.object({
    ...labSchema.shape,
    steps: z.array(z.object({
      ...labSchema.shape.steps.element.shape,
      checks: z.array(checkSchema).max(100),
    }).strict()).max(100),
  }).strict(),
  instructions: z.record(idSchema, text),
  starterFiles: z.record(starterPathSchema, text),
}).strict().refine(doc => JSON.stringify(doc).length <= 8_000_000, "Lab exceeds 8 MB");
export type LabDocument = z.infer<typeof documentSchema>;
export function validatePublication(input: unknown): LabDocument {
  const doc = documentSchema.parse(input);
  const lab = labSchema.parse(doc.definition);
  if (!lab.title.trim() || !lab.description.trim())
    throw new Error("A title and description are required before publishing");
  for (const step of lab.steps) {
    if (!step.title.trim() || !doc.instructions[step.id]?.trim())
      throw new Error(`Step ${step.id} needs a title and instructions`);
  }
  if (!Object.keys(doc.starterFiles).length)
    throw new Error("At least one starter file is required");
  const paths = Object.keys(doc.starterFiles);
  if (paths.some(p => paths.some(other => other.startsWith(p + "/"))))
    throw new Error("A starter file cannot also be a directory");
  return { ...doc, definition: lab };
}
export interface Topic { id: string; title: string; position: number }
export interface CatalogLab {
  id: string; title: string; description: string; topicId: string;
  archived: boolean; publishedVersion?: number; total: number;
}
export interface Catalog { topics: Topic[]; labs: CatalogLab[] }
export interface Draft {
  labId: string; topicId: string; revision: number; document: LabDocument;
}
export const topicSchema = z.object({
  id: idSchema, title: z.string().trim().min(1).max(120),
  position: z.number().int().min(0).max(10000),
}).strict();
export const draftSaveSchema = z.object({
  labId: idSchema, topicId: idSchema, revision: z.number().int().positive(),
  document: documentSchema,
}).strict();

export const catalogSchema = z.object({
  topics: z.array(topicSchema).max(1000),
  labs: z.array(z.object({
    id: idSchema, title: z.string().max(500), description: z.string().max(20000),
    topicId: idSchema, archived: z.boolean(), publishedVersion: z.number().int().positive().optional(),
    total: z.number().int().min(0).max(100),
  }).strict()).max(10000),
}).strict();
export const publicationSchema = z.object({
  labId: idSchema, number: z.number().int().positive(), document: documentSchema,
}).strict();
export type Publication = z.infer<typeof publicationSchema>;
export interface LibraryLab extends CatalogLab {
  key: string; source: string; topic: string; downloadedVersion?: number;
  runVersion?: number; completed: number; hasRun: boolean;
}
export interface Library {
  serverUrl: string; labs: LibraryLab[]; lastSynced?: string; syncError?: string;
  admin: boolean;
}
export function normalizeServerUrl(input: string): string {
  const url = new URL(input);
  const local = ["localhost", "127.0.0.1", "[::1]"].includes(url.hostname);
  if ((url.protocol !== "https:" && !(local && url.protocol === "http:")) ||
      url.username || url.password || url.search || url.hash || url.pathname !== "/")
    throw new Error("Use an HTTPS server origin, or http://localhost:port for development");
  return url.origin;
}
export const serverUrlSchema = z.string().max(2000).transform(normalizeServerUrl);
