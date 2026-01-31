import CodeBlock from "@/components/CodeBlock";
import MarkdownRenderer from "@/components/MarkdownRenderer";
import TableOfContents from "@/components/TableOfContents";
import type { TocHeading } from "@/components/TableOfContents";
import PrevNextNav from "@/components/PrevNextNav";
import { buildNavItems, getAdjacentPages } from "@/lib/navigation";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { notFound } from "next/navigation";

/* ── Markdown cleaning helpers ─────────────────────────── */

function stripTopHeading(markdown: string) {
  const lines = markdown.split(/\r?\n/);
  if (lines.length === 0) return markdown;
  if (!lines[0].trim().startsWith("# ")) return markdown;
  let index = 1;
  while (index < lines.length && lines[index].trim() === "") index += 1;
  return lines.slice(index).join("\n");
}

/** Remove `> Track: ... | Topic: ...` blockquote lines. */
function stripTrackMeta(markdown: string): string {
  return markdown
    .split(/\r?\n/)
    .filter((line) => !/^>\s*Track:\s*`/i.test(line.trim()))
    .join("\n");
}

/** Remove the "## Run tests" section (and everything below it until the next ## heading or EOF). */
function stripRunTests(markdown: string): string {
  const lines = markdown.split(/\r?\n/);
  const result: string[] = [];
  let skipping = false;
  for (const line of lines) {
    if (/^##\s+Run\s+tests/i.test(line)) {
      skipping = true;
      continue;
    }
    if (skipping && /^##\s+/.test(line)) {
      skipping = false;
    }
    if (!skipping) result.push(line);
  }
  return result.join("\n");
}

/**
 * Parse README-style markdown into structured sections.
 * Recognized h2 sections: Concept, Math, Function, Key points.
 * Everything before the first h2 becomes "intro".
 */
interface ContentSection {
  id: string;
  label: string;
  icon: "concept" | "math" | "function" | "keypoints";
  content: string;
}

const SECTION_MAP: Record<string, { label: string; icon: ContentSection["icon"] }> = {
  concept: { label: "Concept", icon: "concept" },
  concepts: { label: "Concepts", icon: "concept" },
  math: { label: "Math", icon: "math" },
  mathematics: { label: "Math", icon: "math" },
  function: { label: "Function", icon: "function" },
  functions: { label: "Functions", icon: "function" },
  api: { label: "Function", icon: "function" },
  "key points": { label: "Key Points", icon: "keypoints" },
  "key-points": { label: "Key Points", icon: "keypoints" },
  keypoints: { label: "Key Points", icon: "keypoints" },
};

function parseSections(markdown: string): { intro: string; sections: ContentSection[] } {
  const lines = markdown.split(/\r?\n/);
  const sections: ContentSection[] = [];
  let intro = "";
  let currentKey: string | null = null;
  let currentLines: string[] = [];

  function flush() {
    if (currentKey !== null) {
      const mapping = SECTION_MAP[currentKey];
      if (mapping) {
        const id = currentKey.replace(/\s+/g, "-");
        sections.push({
          id,
          label: mapping.label,
          icon: mapping.icon,
          content: currentLines.join("\n").trim(),
        });
      } else {
        // Unknown section -- keep as a generic section
        sections.push({
          id: currentKey.replace(/\s+/g, "-"),
          label: currentKey.charAt(0).toUpperCase() + currentKey.slice(1),
          icon: "concept",
          content: currentLines.join("\n").trim(),
        });
      }
    }
    currentLines = [];
  }

  for (const line of lines) {
    const h2 = line.match(/^##\s+(.+)$/);
    if (h2) {
      if (currentKey === null) {
        intro = currentLines.join("\n").trim();
      } else {
        flush();
      }
      currentKey = h2[1].trim().toLowerCase();
      currentLines = [];
    } else {
      currentLines.push(line);
    }
  }
  // Flush last section
  if (currentKey === null) {
    intro = currentLines.join("\n").trim();
  } else {
    flush();
  }

  return { intro, sections };
}

function cleanSummary(summary?: string) {
  if (!summary) return undefined;
  const trimmed = summary.trim();
  if (trimmed.toLowerCase().startsWith("> track")) return undefined;
  return trimmed;
}

function extractHeadings(markdown: string): TocHeading[] {
  const headings: TocHeading[] = [];
  const lines = markdown.split(/\r?\n/);
  for (const line of lines) {
    const match = line.match(/^(#{2,3})\s+(.+)$/);
    if (match) {
      const text = match[2].trim();
      // Skip "Run tests" headings
      if (/^Run\s+tests$/i.test(text)) continue;
      const level = match[1].length;
      const id = text
        .toLowerCase()
        .replace(/[^\w\s-]/g, "")
        .replace(/\s+/g, "-");
      headings.push({ id, text, level });
    }
  }
  return headings;
}

/* ── Section icon SVGs ────────────────────────────────── */

function SectionIcon({ icon }: { icon: ContentSection["icon"] }) {
  switch (icon) {
    case "concept":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <circle cx="8" cy="8" r="6" stroke="currentColor" strokeWidth="1.3" />
          <path d="M8 5v3.5M8 10.5v.5" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "math":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M3 8h10M8 3v10" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
    case "function":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M5.5 4L2 8l3.5 4M10.5 4L14 8l-3.5 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
      );
    case "keypoints":
      return (
        <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
          <path d="M4 4h8M4 8h6M4 12h8" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
        </svg>
      );
  }
}

/* ── Page ─────────────────────────────────────────────── */

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.topics.map((topic) => ({
    track: topic.track,
    topic: topic.topic,
  }));
}

export default async function TopicPage({
  params,
}: {
  params: Promise<{ track: string; topic: string }>;
}) {
  const { track: trackId, topic: topicId } = await params;
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === trackId);
  const topic = content.topics.find(
    (item) => item.track === trackId && item.topic === topicId
  );
  if (!track || !topic) return notFound();

  const navItems = buildNavItems(content);
  const { prev, next } = getAdjacentPages(navItems, trackId, topicId);

  const docs = content.docs
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));
  const modules = content.modules
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));

  const docBySlug = new Map(docs.map((doc) => [doc.slug, doc]));
  const moduleBySlug = new Map(modules.map((module) => [module.slug, module]));
  const entrySlugs = Array.from(
    new Set([
      ...docs.map((doc) => doc.slug),
      ...modules.map((module) => module.slug),
    ])
  );

  const entries = entrySlugs
    .map((slug) => {
      const doc = docBySlug.get(slug);
      const mod = moduleBySlug.get(slug);
      const title = doc?.title ?? mod?.title ?? slug;
      const summary = cleanSummary(doc?.summary) ?? cleanSummary(mod?.summary);

      // Clean the markdown: strip title, track meta, run tests
      let rawContent = doc ? doc.content : mod ? mod.readme : "";
      rawContent = stripTopHeading(rawContent);
      rawContent = stripTrackMeta(rawContent);
      rawContent = stripRunTests(rawContent);

      const parsed = parseSections(rawContent);
      const hasTheory = parsed.intro.length > 0 || parsed.sections.length > 0;
      const codeSources = mod?.sources ?? [];
      const hasCode = codeSources.length > 0;

      return { slug, title, summary, rawContent, parsed, hasTheory, codeSources, hasCode };
    })
    .sort((a, b) => a.title.localeCompare(b.title));

  // Build TOC headings
  const allHeadings: TocHeading[] = [];
  for (const entry of entries) {
    allHeadings.push({ id: entry.slug, text: entry.title, level: 2 });
    for (const section of entry.parsed.sections) {
      allHeadings.push({ id: `${entry.slug}-${section.id}`, text: section.label, level: 3 });
    }
    if (entry.hasCode) {
      allHeadings.push({ id: `${entry.slug}-code`, text: "Demo Code", level: 3 });
    }
  }

  return (
    <div className="handbook-content-wrapper">
      <div>
        {/* Page header */}
        <div className="flex items-center gap-2 mb-1.5">
          <span
            className="h-2 w-2 rounded-full"
            style={{ background: `var(${track.accentVar})` }}
          />
          <span className="text-[0.7rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
            {track.name}
          </span>
        </div>
        <h1 className="text-[1.65rem] font-semibold tracking-tight leading-tight">
          {topic.name}
        </h1>

        {entries.length === 0 ? (
          <div className="empty-state mt-10">
            This topic is waiting on its first concept note or lab.
          </div>
        ) : (
          <div className="mt-8">
            {entries.map((entry, idx) => (
              <article
                key={entry.slug}
                id={entry.slug}
                className="concept-article"
              >
                {idx > 0 && <div className="concept-divider" />}

                <h2 className="concept-title">{entry.title}</h2>
                {entry.summary && (
                  <p className="mt-1 text-[0.85rem] text-[var(--text-secondary)]">
                    {entry.summary}
                  </p>
                )}

                {/* Intro text (before any ## heading) */}
                {entry.parsed.intro && (
                  <div className="mt-3">
                    <MarkdownRenderer content={entry.parsed.intro} />
                  </div>
                )}

                {/* Structured sections */}
                {entry.parsed.sections.map((section) => (
                  <div
                    key={section.id}
                    id={`${entry.slug}-${section.id}`}
                    className="concept-section"
                  >
                    <div className={`section-header section-header-${section.icon}`}>
                      <SectionIcon icon={section.icon} />
                      <span>{section.label}</span>
                    </div>
                    <div className="section-body">
                      <MarkdownRenderer content={section.content} />
                    </div>
                  </div>
                ))}

                {/* Demo code */}
                {entry.hasCode && (
                  <div
                    id={`${entry.slug}-code`}
                    className="concept-section"
                  >
                    <div className="section-header section-header-code">
                      <svg width="14" height="14" viewBox="0 0 16 16" fill="none">
                        <path d="M5.5 4L2 8l3.5 4M10.5 4L14 8l-3.5 4" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" strokeLinejoin="round"/>
                      </svg>
                      <span>Demo Code</span>
                    </div>
                    <div className="section-body">
                      <div className="grid gap-3">
                        {entry.codeSources.map((source) => (
                          <CodeBlock
                            key={source.path}
                            filename={source.path}
                            language={source.language}
                            code={source.content}
                          />
                        ))}
                      </div>
                    </div>
                  </div>
                )}

                {!entry.hasTheory && !entry.hasCode && (
                  <p className="mt-3 text-[0.85rem] text-[var(--text-muted)]">
                    Content coming soon.
                  </p>
                )}
              </article>
            ))}
          </div>
        )}

        <PrevNextNav prev={prev} next={next} />
      </div>

      <TableOfContents headings={allHeadings} />
    </div>
  );
}
