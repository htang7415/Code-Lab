// Content indexer — scans problems meta.json files and generates
// a JSON index for the website.

import { readFileSync, writeFileSync, mkdirSync } from "fs";
import { glob } from "glob";
import { resolve, dirname } from "path";
import { fileURLToPath } from "url";

interface ProblemMeta {
  id: string;
  slug: string;
  title: string;
  track: string;
  topic: string;
  difficulty: string;
  tags: string[];
  languages: string[];
}

async function main() {
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);
  const repoRoot = resolve(__dirname, "../../../../");
  const pattern = "problems/**/meta.json";
  const metaFiles = await glob(pattern, { cwd: repoRoot, absolute: true });

  const problems: ProblemMeta[] = [];

  for (const filePath of metaFiles.sort()) {
    try {
      const raw = readFileSync(filePath, "utf-8");
      const meta: ProblemMeta = JSON.parse(raw);
      problems.push(meta);
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  const outDir = resolve(repoRoot, "web/apps/site/src/content");
  mkdirSync(outDir, { recursive: true });

  const outPath = resolve(outDir, "problems_index.json");
  writeFileSync(outPath, JSON.stringify(problems, null, 2) + "\n");

  console.log(`Indexed ${problems.length} problem(s) → ${outPath}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
