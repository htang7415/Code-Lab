import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";

export default function Home() {
  const content = contentData as ContentIndex;
  const { tracks, topics, modules } = content;

  return (
    <div>
      <h1 className="text-2xl font-semibold tracking-tight">
        Welcome to Code Lab
      </h1>
      <p className="mt-2 text-[0.92rem] text-[var(--text-secondary)] leading-relaxed max-w-xl">
        A structured handbook for learning computer science fundamentals.
        Each topic pairs clear explanations with runnable demo code.
      </p>

      <div className="mt-3 flex gap-4 text-[0.78rem] text-[var(--text-muted)]">
        <span>{tracks.length} tracks</span>
        <span>&middot;</span>
        <span>{topics.length} topics</span>
        <span>&middot;</span>
        <span>{modules.length} code labs</span>
      </div>

      <div className="mt-8 space-y-4">
        {tracks.map((track) => {
          const trackTopics = topics
            .filter((t) => t.track === track.id)
            .sort((a, b) => a.name.localeCompare(b.name));

          return (
            <section key={track.id} className="track-section">
              <div className="track-section-header">
                <span
                  className="track-section-dot"
                  style={{ background: `var(${track.accentVar})` }}
                />
                <Link
                  href={`/track/${track.id}`}
                  className="text-[0.92rem] font-semibold tracking-tight hover:text-[var(--accent)]"
                >
                  {track.name}
                </Link>
                <span className="track-section-count">
                  {trackTopics.length} topics
                </span>
              </div>
              <p className="text-[0.8rem] text-[var(--text-muted)] mb-1">
                {track.description}
              </p>
              <div className="track-topic-grid">
                {trackTopics.map((topic) => (
                  <Link
                    key={topic.topic}
                    href={`/track/${track.id}/${topic.topic}`}
                    className="track-topic-link"
                  >
                    {topic.name}
                  </Link>
                ))}
              </div>
            </section>
          );
        })}
      </div>
    </div>
  );
}
