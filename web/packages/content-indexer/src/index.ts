// Content indexer — builds a unified content index for the website.

import {
  readFileSync,
  writeFileSync,
  mkdirSync,
  statSync,
  existsSync,
} from "fs";
import { glob } from "glob";
import { resolve, dirname, relative, basename, extname } from "path";
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

interface ProblemIndexEntry extends ProblemMeta {
  path: string;
  summary?: string;
  statement: string;
}

interface ModuleSource {
  path: string;
  language: string;
  content: string;
}

interface ModuleIndexEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  readme: string;
  sources: ModuleSource[];
}

interface DocIndexEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  content: string;
}

interface SearchEntry {
  id: string;
  type: "module" | "doc";
  title: string;
  summary?: string;
  track: string;
  topic: string;
  slug: string;
  href: string;
  trackName: string;
  topicName: string;
}

interface TopicIndexEntry {
  track: string;
  topic: string;
  name: string;
  path: string;
  hasDoc: boolean;
  docCount: number;
  moduleCount: number;
  problemCount: number;
}

interface TrackIndexEntry {
  id: string;
  name: string;
  description: string;
  accent: string;
  accentVar: string;
  topicCount: number;
  moduleCount: number;
  problemCount: number;
}

interface ContentIndex {
  generated_at: string;
  tracks: TrackIndexEntry[];
  topics: TopicIndexEntry[];
  modules: ModuleIndexEntry[];
  problems: ProblemIndexEntry[];
  docs: DocIndexEntry[];
}

interface SearchIndex {
  generated_at: string;
  entries: SearchEntry[];
}

const TRACKS: Array<Omit<TrackIndexEntry, "topicCount" | "moduleCount" | "problemCount">> = [
  {
    id: "dsa",
    name: "Data Structures & Algorithms",
    description: "Core patterns, data structures, and problem-solving speed.",
    accent: "#38bdf8",
    accentVar: "--track-dsa",
  },
  {
    id: "ml",
    name: "Machine Learning",
    description: "Math foundations, models, optimization, and systems.",
    accent: "#a78bfa",
    accentVar: "--track-ml",
  },
  {
    id: "ai-agents",
    name: "AI Agents",
    description: "Prompting, tool use, memory, and evaluation.",
    accent: "#34d399",
    accentVar: "--track-ai-agents",
  },
  {
    id: "databases",
    name: "Databases",
    description: "Schema design, indexing, transactions, and query plans.",
    accent: "#fbbf24",
    accentVar: "--track-databases",
  },
  {
    id: "software-engineering",
    name: "Software Engineering",
    description: "APIs, performance, testing, and system design.",
    accent: "#fb7185",
    accentVar: "--track-se",
  },
];

const TOPIC_NAMES: Record<string, string> = {
  dp: "Dynamic Programming",
  llm: "LLM",
  mlops: "MLOps",
  gnn: "Graph Neural Networks",
  cnn: "Convolutional Neural Networks",
  rnn: "Recurrent Neural Networks",
  mlp: "Multi-Layer Perceptrons",
  vae: "Variational Autoencoders",
  ai: "AI",
  api: "API",
  apis: "APIs",
  sql: "SQL",
  gpu: "GPU",
  cv: "Cross Validation",
  rl: "Reinforcement Learning",
  "rl-for-llm": "RL for LLM",
};

const MAX_SUMMARY_LENGTH = 180;

function isDirectory(path: string) {
  try {
    return statSync(path).isDirectory();
  } catch {
    return false;
  }
}

function kebabToTitle(value: string) {
  const lower = value.toLowerCase();
  if (TOPIC_NAMES[lower]) return TOPIC_NAMES[lower];
  return value
    .split("-")
    .map((part) => {
      const key = part.toLowerCase();
      if (TOPIC_NAMES[key]) return TOPIC_NAMES[key];
      return part.charAt(0).toUpperCase() + part.slice(1);
    })
    .join(" ");
}

function extractTitle(markdown: string, fallback: string) {
  const match = markdown.match(/^#\s+(.+)$/m);
  return match ? match[1].trim() : fallback;
}

function extractSummary(markdown: string) {
  const lines = markdown.split(/\r?\n/);
  let inCode = false;
  const paragraph: string[] = [];

  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed.startsWith("```")) {
      inCode = !inCode;
      continue;
    }
    if (inCode) continue;
    if (!trimmed) {
      if (paragraph.length > 0) break;
      continue;
    }
    if (trimmed.startsWith("#")) continue;
    paragraph.push(trimmed);
  }

  if (paragraph.length === 0) return undefined;
  const summary = paragraph.join(" ").replace(/\s+/g, " ").trim();
  if (summary.length <= MAX_SUMMARY_LENGTH) return summary;
  return `${summary.slice(0, MAX_SUMMARY_LENGTH).trim()}…`;
}

function loadMarkdown(filePath: string) {
  return readFileSync(filePath, "utf-8");
}

function languageFromPath(filePath: string) {
  const extension = extname(filePath);
  if (extension === ".py") return "python";
  if (extension === ".rs") return "rust";
  if (extension === ".ts" || extension === ".tsx") return "typescript";
  return extension.replace(".", "") || "text";
}

async function main() {
  const __filename = fileURLToPath(import.meta.url);
  const __dirname = dirname(__filename);
  const repoRoot = resolve(__dirname, "../../../../");

  const problemsPattern = "problems/**/meta.json";
  const modulesPattern = "modules/**/README.md";
  const docsPattern = "docs/**/*.md";
  const topicsPattern = "docs/*/*";

  const metaFiles = await glob(problemsPattern, {
    cwd: repoRoot,
    absolute: true,
    nodir: true,
  });
  const moduleFiles = await glob(modulesPattern, {
    cwd: repoRoot,
    absolute: true,
    nodir: true,
  });
  const docFiles = await glob(docsPattern, {
    cwd: repoRoot,
    absolute: true,
    nodir: true,
  });
  const topicDirs = (await glob(topicsPattern, {
    cwd: repoRoot,
    absolute: true,
  })).filter(isDirectory);

  const problems: ProblemIndexEntry[] = [];
  const modules: ModuleIndexEntry[] = [];
  const docs: DocIndexEntry[] = [];

  for (const filePath of metaFiles.sort()) {
    try {
      const raw = readFileSync(filePath, "utf-8");
      const meta: ProblemMeta = JSON.parse(raw);
      const problemDir = dirname(filePath);
      const problemPath = relative(repoRoot, problemDir);
      const statementPath = resolve(problemDir, "problem.md");
      const statement = existsSync(statementPath)
        ? readFileSync(statementPath, "utf-8")
        : "";
      const summary = statement ? extractSummary(statement) : undefined;
      problems.push({
        ...meta,
        path: problemPath,
        summary,
        statement,
      });
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  for (const filePath of moduleFiles.sort()) {
    try {
      const relPath = relative(repoRoot, filePath);
      const parts = relPath.split("/");
      if (parts.length < 5) continue;
      const track = parts[1];
      const topic = parts[2];
      const slug = parts[3];
      const moduleDir = dirname(filePath);
      const readme = loadMarkdown(filePath);
      const title = extractTitle(readme, kebabToTitle(slug));
      const summary = extractSummary(readme);

      const sources: ModuleSource[] = [];
      const pythonSources = await glob("python/**/*.py", {
        cwd: moduleDir,
        absolute: true,
        nodir: true,
      });
      for (const sourcePath of pythonSources) {
        const fileName = basename(sourcePath);
        if (fileName.startsWith("test_")) continue;
        if (sourcePath.includes("__pycache__")) continue;
        sources.push({
          path: relative(repoRoot, sourcePath),
          language: languageFromPath(sourcePath),
          content: readFileSync(sourcePath, "utf-8"),
        });
      }

      const rustSources = await glob("rust/src/**/*.rs", {
        cwd: moduleDir,
        absolute: true,
        nodir: true,
      });
      for (const sourcePath of rustSources) {
        sources.push({
          path: relative(repoRoot, sourcePath),
          language: languageFromPath(sourcePath),
          content: readFileSync(sourcePath, "utf-8"),
        });
      }

      modules.push({
        track,
        topic,
        slug,
        title,
        path: relative(repoRoot, moduleDir),
        summary,
        readme,
        sources,
      });
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  for (const filePath of docFiles.sort()) {
    try {
      const relPath = relative(repoRoot, filePath);
      const parts = relPath.split("/");
      if (parts.length < 3) continue;
      const track = parts[1];
      const topic = parts[2];
      let slug = basename(filePath, ".md");
      if (slug.toLowerCase() === "readme" && parts.length >= 4) {
        slug = parts[parts.length - 2];
      }
      const markdown = loadMarkdown(filePath);
      const title = extractTitle(markdown, kebabToTitle(slug));
      const summary = extractSummary(markdown);
      docs.push({
        track,
        topic,
        slug,
        title,
        path: relPath,
        summary,
        content: markdown,
      });
    } catch (err) {
      console.error(`Warning: could not parse ${filePath}:`, err);
    }
  }

  const docCountByTopic = new Map<string, number>();
  for (const doc of docs) {
    const key = `${doc.track}/${doc.topic}`;
    docCountByTopic.set(key, (docCountByTopic.get(key) ?? 0) + 1);
  }
  const moduleCountByTopic = new Map<string, number>();
  for (const module of modules) {
    const key = `${module.track}/${module.topic}`;
    moduleCountByTopic.set(key, (moduleCountByTopic.get(key) ?? 0) + 1);
  }
  const problemCountByTopic = new Map<string, number>();
  for (const problem of problems) {
    const key = `${problem.track}/${problem.topic}`;
    problemCountByTopic.set(key, (problemCountByTopic.get(key) ?? 0) + 1);
  }

  const trackNameById = new Map(TRACKS.map((track) => [track.id, track.name]));
  const searchEntries: SearchEntry[] = [];
  for (const module of modules) {
    const trackName = trackNameById.get(module.track) ?? kebabToTitle(module.track);
    const topicName = kebabToTitle(module.topic);
    searchEntries.push({
      id: `module:${module.track}/${module.topic}/${module.slug}`,
      type: "module",
      title: module.title,
      summary: module.summary,
      track: module.track,
      topic: module.topic,
      slug: module.slug,
      href: `/track/${module.track}/${module.topic}#${module.slug}`,
      trackName,
      topicName,
    });
  }
  for (const doc of docs) {
    const trackName = trackNameById.get(doc.track) ?? kebabToTitle(doc.track);
    const topicName = kebabToTitle(doc.topic);
    searchEntries.push({
      id: `doc:${doc.track}/${doc.topic}/${doc.slug}`,
      type: "doc",
      title: doc.title,
      summary: doc.summary,
      track: doc.track,
      topic: doc.topic,
      slug: doc.slug,
      href: `/track/${doc.track}/${doc.topic}#${doc.slug}`,
      trackName,
      topicName,
    });
  }

  const topics: TopicIndexEntry[] = topicDirs
    .map((dirPath) => {
      const relPath = relative(repoRoot, dirPath);
      const parts = relPath.split("/");
      const track = parts[1];
      const topic = parts[2];
      const key = `${track}/${topic}`;
      const docCount = docCountByTopic.get(key) ?? 0;
      const moduleCount = moduleCountByTopic.get(key) ?? 0;
      const problemCount = problemCountByTopic.get(key) ?? 0;
      return {
        track,
        topic,
        name: kebabToTitle(topic),
        path: `/track/${track}/${topic}`,
        hasDoc: docCount > 0,
        docCount,
        moduleCount,
        problemCount,
      };
    })
    .filter((topic) => Boolean(topic.track) && Boolean(topic.topic))
    .sort((a, b) => a.name.localeCompare(b.name));

  const tracks: TrackIndexEntry[] = TRACKS.map((track) => {
    const topicCount = topics.filter((topic) => topic.track === track.id).length;
    const moduleCount = modules.filter((module) => module.track === track.id).length;
    const problemCount = problems.filter((problem) => problem.track === track.id).length;
    return {
      ...track,
      topicCount,
      moduleCount,
      problemCount,
    };
  });

  const outDir = resolve(repoRoot, "web/apps/site/src/content");
  mkdirSync(outDir, { recursive: true });
  const generatedAt = new Date().toISOString();

  const contentIndex: ContentIndex = {
    generated_at: generatedAt,
    tracks,
    topics,
    modules,
    problems,
    docs,
  };

  const contentPath = resolve(outDir, "content_index.json");
  writeFileSync(contentPath, JSON.stringify(contentIndex, null, 2) + "\n");

  const problemsIndex = {
    generated_at: generatedAt,
    problems,
  };
  const problemsPath = resolve(outDir, "problems_index.json");
  writeFileSync(problemsPath, JSON.stringify(problemsIndex, null, 2) + "\n");

  const searchIndex: SearchIndex = {
    generated_at: generatedAt,
    entries: searchEntries
      .slice()
      .sort((a, b) => a.title.localeCompare(b.title)),
  };
  const searchPath = resolve(outDir, "search_index.json");
  writeFileSync(searchPath, JSON.stringify(searchIndex, null, 2) + "\n");

  console.log(
    `Indexed ${problems.length} problem(s), ${modules.length} module(s), ${docs.length} doc(s)`
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
