import Link from "next/link";
import searchData from "@/content/search_index.json";
import type { SearchEntry, SearchIndex } from "@/lib/search";

function normalizeQuery(value: string) {
  return value.trim().toLowerCase();
}

const STOPWORDS = new Set([
  "a",
  "an",
  "the",
  "and",
  "or",
  "of",
  "to",
  "in",
  "for",
  "on",
  "with",
  "by",
  "at",
  "from",
  "into",
  "about",
  "as",
  "is",
  "are",
  "was",
  "were",
  "be",
  "been",
  "being",
  "function",
  "functions",
]);

function tokenize(value: string) {
  return normalizeQuery(value)
    .split(/[^a-z0-9]+/)
    .filter(Boolean)
    .filter((token) => !STOPWORDS.has(token));
}

function splitWords(value: string) {
  return normalizeQuery(value).split(/[^a-z0-9]+/).filter(Boolean);
}

function editDistance(a: string, b: string) {
  if (a === b) return 0;
  const alen = a.length;
  const blen = b.length;
  if (alen === 0) return blen;
  if (blen === 0) return alen;

  const dp = new Array(alen + 1).fill(0);
  for (let i = 0; i <= alen; i += 1) dp[i] = i;

  for (let j = 1; j <= blen; j += 1) {
    let prev = dp[0];
    dp[0] = j;
    for (let i = 1; i <= alen; i += 1) {
      const temp = dp[i];
      const cost = a[i - 1] === b[j - 1] ? 0 : 1;
      dp[i] = Math.min(
        dp[i] + 1,
        dp[i - 1] + 1,
        prev + cost
      );
      prev = temp;
    }
  }
  return dp[alen];
}

function tokenMatches(token: string, haystack: string, words: string[]) {
  if (haystack.includes(token)) return true;

  const len = token.length;
  const threshold = len >= 8 ? 2 : len >= 5 ? 1 : 0;
  if (threshold === 0) return false;

  for (const word of words) {
    if (Math.abs(word.length - len) > threshold) continue;
    if (editDistance(token, word) <= threshold) return true;
  }
  return false;
}

function scoreEntry(entry: SearchEntry, query: string, tokens: string[]) {
  const title = entry.title.toLowerCase();
  const summary = (entry.summary ?? "").toLowerCase();
  const topic = entry.topicName.toLowerCase();
  const track = entry.trackName.toLowerCase();
  const haystack = `${title} ${summary} ${topic} ${track}`;
  const words = splitWords(haystack);

  if (!tokens.every((token) => tokenMatches(token, haystack, words))) return 0;

  let score = 0;
  if (title.includes(query)) score += 6;
  if (summary.includes(query)) score += 2;
  if (`${topic} ${track}`.includes(query)) score += 3;

  for (const token of tokens) {
    if (title.includes(token)) score += 3;
    else if (tokenMatches(token, title, splitWords(title))) score += 2;

    if (summary.includes(token)) score += 1;
    else if (summary && tokenMatches(token, summary, splitWords(summary))) score += 0.5;

    if (topic.includes(token) || track.includes(token)) score += 2;
    else if (
      tokenMatches(token, topic, splitWords(topic)) ||
      tokenMatches(token, track, splitWords(track))
    ) {
      score += 1;
    }
  }

  return score;
}

export default async function SearchPage({
  searchParams,
}: {
  searchParams?: Promise<{ q?: string | string[] }>;
}) {
  const resolvedSearchParams = await searchParams;
  const raw =
    typeof resolvedSearchParams?.q === "string" ? resolvedSearchParams.q : "";
  const query = normalizeQuery(raw);
  const cleanedTokens = tokenize(raw);
  const tokens =
    cleanedTokens.length > 0 ? cleanedTokens : query ? [query] : [];
  const searchIndex = searchData as SearchIndex;
  const entries = searchIndex.entries as SearchEntry[];

  const results =
    query.length === 0
      ? []
      : entries
          .map((entry) => ({
            entry,
            score: scoreEntry(entry, query, tokens),
          }))
          .filter((item) => item.score > 0)
          .sort(
            (a, b) =>
              b.score - a.score || a.entry.title.localeCompare(b.entry.title)
          )
          .map((item) => item.entry);

  return (
    <div className="search-page">
      <div className="search-hero">
        <h1 className="text-2xl font-semibold tracking-tight">Search</h1>
        <p className="mt-2 text-[0.9rem] text-[var(--text-secondary)]">
          Find docs and demos across tracks.
        </p>
        <form action="/search" className="search-form" role="search">
          <input
            type="search"
            name="q"
            placeholder="Search topics, concepts, or demos"
            defaultValue={raw}
            className="search-input"
            autoFocus
            aria-label="Search topics"
          />
          <button className="search-button" type="submit">
            Search
          </button>
        </form>
        <p className="search-meta">
          {query
            ? `${results.length} result${results.length === 1 ? "" : "s"} for "${raw}"`
            : `${entries.length} searchable entries`}
        </p>
      </div>

      {query.length === 0 ? (
        <div className="search-empty">
          Type a query above to start exploring.
        </div>
      ) : results.length === 0 ? (
        <div className="search-empty">
          No matches. Try a shorter query or different wording.
        </div>
      ) : (
        <div className="search-results">
          {results.map((entry) => (
            <Link
              key={entry.id}
              href={entry.href}
              className="search-result-card"
              data-parallax="6"
            >
              <div className="search-result-meta">
                <span className="search-result-kind">
                  {entry.type === "doc" ? "Doc" : "Demo"}
                </span>
                <span>
                  {entry.trackName} / {entry.topicName}
                </span>
              </div>
              <div className="search-result-title">{entry.title}</div>
              {entry.summary && (
                <div className="search-result-summary">{entry.summary}</div>
              )}
            </Link>
          ))}
        </div>
      )}
    </div>
  );
}
