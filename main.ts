// Entry program for post-x-promote-make-your-own-bounty-01 (Node 22+, stdlib only).
//
// The entry itself is an X post: one post of the entrant's own that quotes
// make.fun's make-your-own-bounty post (https://x.com/makefunai/status/2124915864336236646)
// or links to it, with a photo of its own attached, make.fun or the @makefunai
// tag and the entrant's play code in its text. POST.json at the repository
// root names that post. All this program does is copy POST.json into the
// output directory, where the gate reads it. The house reads the post itself
// from X; nothing this program writes about the post is scored.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(botDir, "POST.json");
const target = join(outDir, "POST.json");

if (!existsSync(source)) {
  console.error(`POST.json not found in ${botDir}`);
  process.exit(1);
}

let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(source, "utf8"));
} catch (err) {
  console.error(`POST.json is not valid JSON: ${(err as Error).message}`);
  process.exit(1);
}

const url =
  parsed !== null && typeof parsed === "object"
    ? (parsed as Record<string, unknown>).url
    : undefined;
if (typeof url !== "string" || !/^https:\/\/(x\.com|twitter\.com)\/\S+\/status\/\d+$/.test(url)) {
  console.error(
    `Invalid post URL in ${source}: ${JSON.stringify(url)} — expected "https://x.com/<handle>/status/<id>", e.g. "https://x.com/pemburudollar05/status/2125032201687548026"`,
  );
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

// Verify the copy landed byte-identical; a truncated or partial copy
// must fail loudly instead of being scored as a corrupt entry.
if (!readFileSync(target).equals(readFileSync(source))) {
  console.error(`Copy verification failed: ${target} differs from ${source}`);
  process.exit(1);
}
