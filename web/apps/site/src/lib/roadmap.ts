import type { Track, Topic } from "./content";

const TRACK_ORDER = [
  "dsa",
  "software-engineering",
  "databases",
  "ml",
  "ai-agents",
];

const TOPIC_ORDER: Record<string, string[]> = {
  "dsa": [
    "arrays",
    "strings",
    "linked-list",
    "stack-queue",
    "hashing",
    "sorting",
    "binary-search",
    "recursion",
    "trees",
    "tries",
    "heap",
    "intervals",
    "greedy",
    "backtracking",
    "dp",
    "graphs",
    "shortest-path",
    "topo-sort",
    "union-find",
    "bit",
    "math",
  ],
  "software-engineering": [
    "tooling",
    "python",
    "rust",
    "testing",
    "apis",
    "security-basics",
    "performance",
    "concurrency",
    "design-patterns",
    "system-design",
  ],
  "databases": [
    "relational",
    "schema-design",
    "sql-patterns",
    "indexing",
    "transactions",
    "query-plans",
    "caching",
    "nosql",
    "streaming",
    "vector-db",
  ],
  "ml": [
    "fundamentals",
    "data",
    "models",
    "evaluation",
    "optimization",
    "deep-learning",
    "systems",
    "representation",
    "generative",
    "computer-vision",
    "llm",
    "reinforcement-learning",
    "mlops",
  ],
  "ai-agents": [
    "prompting",
    "tool-use",
    "rag",
    "memory",
    "planning",
    "multi-agent",
    "evals",
    "observability",
    "guardrails",
  ],
};

function buildRankMap(order: string[]) {
  const map = new Map<string, number>();
  order.forEach((id, index) => map.set(id, index));
  return map;
}

const TRACK_RANK = buildRankMap(TRACK_ORDER);
const TOPIC_RANKS = new Map(
  Object.entries(TOPIC_ORDER).map(([trackId, order]) => [trackId, buildRankMap(order)])
);

export function sortTracks(tracks: Track[]): Track[] {
  return tracks.slice().sort((a, b) => {
    const rankA = TRACK_RANK.get(a.id) ?? Number.MAX_SAFE_INTEGER;
    const rankB = TRACK_RANK.get(b.id) ?? Number.MAX_SAFE_INTEGER;
    if (rankA !== rankB) return rankA - rankB;
    return a.name.localeCompare(b.name);
  });
}

export function sortTopics(topics: Topic[]): Topic[] {
  return topics.slice().sort((a, b) => {
    const trackRankA = TRACK_RANK.get(a.track) ?? Number.MAX_SAFE_INTEGER;
    const trackRankB = TRACK_RANK.get(b.track) ?? Number.MAX_SAFE_INTEGER;
    if (trackRankA !== trackRankB) return trackRankA - trackRankB;

    const topicRank = TOPIC_RANKS.get(a.track);
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;

    return a.name.localeCompare(b.name);
  });
}

export function sortTopicsForTrack(topics: Topic[], trackId: string): Topic[] {
  const topicRank = TOPIC_RANKS.get(trackId);
  return topics.slice().sort((a, b) => {
    const rankA = topicRank?.get(a.topic);
    const rankB = topicRank?.get(b.topic);
    if (rankA != null && rankB != null) return rankA - rankB;
    if (rankA != null) return -1;
    if (rankB != null) return 1;
    return a.name.localeCompare(b.name);
  });
}

export function extractModuleOrder(
  docContent: string | undefined,
  trackId: string,
  topicId: string
): string[] {
  if (!docContent) return [];
  const pattern = new RegExp(`modules/${trackId}/${topicId}/([a-z0-9-]+)`, "g");
  const order: string[] = [];
  const seen = new Set<string>();
  let match: RegExpExecArray | null;
  while ((match = pattern.exec(docContent)) !== null) {
    const slug = match[1];
    if (!seen.has(slug)) {
      seen.add(slug);
      order.push(slug);
    }
  }
  return order;
}
