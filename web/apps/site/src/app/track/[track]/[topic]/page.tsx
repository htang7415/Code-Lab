import Breadcrumb from "@/components/Breadcrumb";
import CodeBlock from "@/components/CodeBlock";
import MarkdownRenderer from "@/components/MarkdownRenderer";
import ProblemTable from "@/components/ProblemTable";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { notFound } from "next/navigation";

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.topics.map((topic) => ({
    track: topic.track,
    topic: topic.topic,
  }));
}

export default function TopicPage({
  params,
}: {
  params: { track: string; topic: string };
}) {
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === params.track);
  const topic = content.topics.find(
    (item) => item.track === params.track && item.topic === params.topic
  );
  if (!track || !topic) return notFound();

  const docs = content.docs
    .filter((item) => item.track === params.track && item.topic === params.topic)
    .sort((a, b) => a.title.localeCompare(b.title));
  const modules = content.modules
    .filter((item) => item.track === params.track && item.topic === params.topic)
    .sort((a, b) => a.title.localeCompare(b.title));
  const problems = content.problems
    .filter((item) => item.track === params.track && item.topic === params.topic)
    .sort((a, b) => a.title.localeCompare(b.title));

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <div
        className="mb-8 h-1 w-16 rounded-full"
        style={{ background: `var(${track.accentVar})` }}
      />
      <Breadcrumb
        items={[
          { label: "home", href: "/" },
          { label: params.track, href: `/track/${params.track}` },
          { label: params.topic },
        ]}
      />
      <div className="mt-6">
        <h1 className="text-3xl font-semibold">{topic.name}</h1>
        <p className="mt-2 text-sm text-[var(--text-secondary)]">
          Deep dive notes, hands-on labs, and practice problems.
        </p>
      </div>

      <section className="mt-12">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-semibold">Concept Notes</h2>
          <span className="badge font-mono">{docs.length} notes</span>
        </div>
        <div className="mt-6 grid gap-6">
          {docs.length === 0 ? (
            <div className="surface-card p-6 text-sm text-[var(--text-muted)]">
              Notes for this topic are coming soon.
            </div>
          ) : (
            docs.map((doc) => (
              <div key={doc.path} className="surface-card p-6">
                <h3 className="text-lg font-semibold">{doc.title}</h3>
                {doc.summary && (
                  <p className="mt-2 text-sm text-[var(--text-secondary)]">
                    {doc.summary}
                  </p>
                )}
                <div className="mt-4">
                  <MarkdownRenderer content={doc.content} />
                </div>
              </div>
            ))
          )}
        </div>
      </section>

      <section className="mt-12">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-semibold">Code Labs</h2>
          <span className="badge font-mono">{modules.length} labs</span>
        </div>
        <div className="mt-6 grid gap-6">
          {modules.length === 0 ? (
            <div className="surface-card p-6 text-sm text-[var(--text-muted)]">
              Labs for this topic are coming soon.
            </div>
          ) : (
            modules.map((module) => (
              <div key={module.path} className="surface-card p-6">
                <div className="flex flex-wrap items-center justify-between gap-4">
                  <div>
                    <p className="font-mono text-xs uppercase tracking-[0.2em] text-[var(--text-muted)]">
                      {module.slug}
                    </p>
                    <h3 className="mt-2 text-lg font-semibold">
                      {module.title}
                    </h3>
                    {module.summary && (
                      <p className="mt-2 text-sm text-[var(--text-secondary)]">
                        {module.summary}
                      </p>
                    )}
                  </div>
                </div>
                <div className="mt-4">
                  <MarkdownRenderer content={module.readme} />
                </div>
                {module.sources.length > 0 && (
                  <div className="mt-6 grid gap-4">
                    {module.sources.map((source) => (
                      <CodeBlock
                        key={source.path}
                        filename={source.path}
                        language={source.language}
                        code={source.content}
                      />
                    ))}
                  </div>
                )}
              </div>
            ))
          )}
        </div>
      </section>

      <section className="mt-12">
        <div className="flex items-center justify-between">
          <h2 className="text-xl font-semibold">Practice Problems</h2>
          <span className="badge font-mono">{problems.length} problems</span>
        </div>
        <div className="mt-6">
          <ProblemTable problems={problems} />
        </div>
      </section>
    </div>
  );
}
