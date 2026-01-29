import Breadcrumb from "@/components/Breadcrumb";
import CodeBlock from "@/components/CodeBlock";
import MarkdownRenderer from "@/components/MarkdownRenderer";
import ProblemTable from "@/components/ProblemTable";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { notFound } from "next/navigation";
import type { CSSProperties } from "react";

function stripTopHeading(markdown: string) {
  const lines = markdown.split(/\r?\n/);
  if (lines.length === 0) return markdown;
  if (!lines[0].trim().startsWith("# ")) return markdown;
  let index = 1;
  while (index < lines.length && lines[index].trim() === "") {
    index += 1;
  }
  return lines.slice(index).join("\n");
}

function cleanSummary(summary?: string) {
  if (!summary) return undefined;
  const trimmed = summary.trim();
  if (trimmed.toLowerCase().startsWith("> track")) return undefined;
  return trimmed;
}

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

  const docs = content.docs
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));
  const modules = content.modules
    .filter((item) => item.track === trackId && item.topic === topicId)
    .sort((a, b) => a.title.localeCompare(b.title));
  const problems = content.problems
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
      const module = moduleBySlug.get(slug);
      const title = doc?.title ?? module?.title ?? slug;
      const summary = cleanSummary(doc?.summary) ?? cleanSummary(module?.summary);
      const theoryContent = doc
        ? stripTopHeading(doc.content)
        : module
          ? stripTopHeading(module.readme)
          : "";
      const hasTheory = Boolean(theoryContent.trim());
      const codeSources = module?.sources ?? [];
      const hasCode = codeSources.length > 0;
      return {
        slug,
        title,
        summary,
        theoryContent,
        hasTheory,
        codeSources,
        hasCode,
      };
    })
    .sort((a, b) => a.title.localeCompare(b.title));

  const codeCount = entries.filter((entry) => entry.hasCode).length;
  const accentStyle = {
    ["--handbook-accent" as string]: `var(${track.accentVar})`,
  } satisfies CSSProperties;

  return (
    <div className="pb-16" style={accentStyle}>
      <section className="relative overflow-hidden border-b border-[var(--border-primary)] bg-white">
        <div className="hero-grid absolute inset-0" />
        <div className="relative mx-auto max-w-7xl px-6 py-12">
          <div
            className="mb-6 h-1 w-16 rounded-full"
            style={{ background: `var(${track.accentVar})` }}
          />
          <Breadcrumb
            items={[
              { label: "home", href: "/" },
              { label: trackId, href: `/track/${trackId}` },
              { label: topicId },
            ]}
          />
          <p className="mt-6 font-mono text-xs uppercase tracking-[0.4em] text-[var(--text-muted)]">
            Handbook · {track.name}
          </p>
          <h1 className="mt-3 text-3xl font-semibold md:text-4xl">
            {topic.name}
          </h1>
          <p className="mt-3 max-w-2xl text-sm text-[var(--text-secondary)] md:text-base">
            Theory and runnable code on the same page. Scan the concepts, copy
            the demos, then lock it in with practice.
          </p>
          <div className="mt-8 flex flex-wrap gap-4">
            <div className="stat-chip">
              <span className="text-2xl font-semibold">{entries.length}</span>
              <span className="text-xs text-[var(--text-muted)]">
                Concepts
              </span>
            </div>
            <div className="stat-chip">
              <span className="text-2xl font-semibold">{codeCount}</span>
              <span className="text-xs text-[var(--text-muted)]">
                Code demos
              </span>
            </div>
            <div className="stat-chip">
              <span className="text-2xl font-semibold">
                {problems.length}
              </span>
              <span className="text-xs text-[var(--text-muted)]">
                Practice problems
              </span>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-6 pt-12">
        {entries.length === 0 ? (
          <div className="surface-card p-6 text-sm text-[var(--text-muted)]">
            This topic is waiting on its first concept note or lab. Add a doc or
            module to see the handbook view.
          </div>
        ) : (
          <div className="grid gap-10 lg:grid-cols-[260px_minmax(0,1fr)]">
            <aside className="handbook-nav">
              <div className="surface-card p-4">
                <p className="font-mono text-xs uppercase tracking-[0.3em] text-[var(--text-muted)]">
                  In this topic
                </p>
                <nav className="mt-4 flex flex-col gap-2">
                  {entries.map((entry) => (
                    <a
                      key={entry.slug}
                      href={`#${entry.slug}`}
                      className="handbook-nav-link"
                    >
                      <span className="handbook-dot" />
                      <span className="flex-1 text-sm">{entry.title}</span>
                      <span className="text-xs text-[var(--text-muted)]">
                        {entry.hasCode ? "code" : "notes"}
                      </span>
                    </a>
                  ))}
                  <a href="#practice" className="handbook-nav-link">
                    <span className="handbook-dot handbook-dot-accent" />
                    <span className="flex-1 text-sm">Practice</span>
                    <span className="text-xs text-[var(--text-muted)]">
                      {problems.length}
                    </span>
                  </a>
                </nav>
              </div>
            </aside>

            <div className="space-y-10">
              {entries.map((entry) => (
                <article
                  key={entry.slug}
                  id={entry.slug}
                  className="handbook-entry surface-card p-6 md:p-8"
                >
                  <header>
                    <p className="font-mono text-xs uppercase tracking-[0.2em] text-[var(--text-muted)]">
                      {entry.slug}
                    </p>
                    <h2 className="mt-2 text-2xl font-semibold">
                      {entry.title}
                    </h2>
                    {entry.summary && (
                      <p className="mt-2 text-sm text-[var(--text-secondary)]">
                        {entry.summary}
                      </p>
                    )}
                  </header>

                  <div className="mt-6">
                    {entry.hasTheory ? (
                      <MarkdownRenderer content={entry.theoryContent} />
                    ) : (
                      <p className="text-sm text-[var(--text-muted)]">
                        Theory notes are coming soon for this concept.
                      </p>
                    )}

                    {entry.hasCode && (
                      <div className="mt-8">
                        <p className="implementation-label mb-4">Implementation</p>
                        <div className="grid gap-4">
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
                    )}
                  </div>
                </article>
              ))}

              <section id="practice" className="handbook-entry surface-card p-6">
                <div className="flex flex-wrap items-center justify-between gap-4">
                  <div>
                    <h2 className="text-xl font-semibold">Practice problems</h2>
                    <p className="mt-2 text-sm text-[var(--text-secondary)]">
                      Reinforce the concepts with targeted exercises.
                    </p>
                  </div>
                  <span className="badge font-mono">
                    {problems.length} problems
                  </span>
                </div>
                <div className="mt-6">
                  <ProblemTable problems={problems} />
                </div>
              </section>
            </div>
          </div>
        )}
      </section>
    </div>
  );
}
