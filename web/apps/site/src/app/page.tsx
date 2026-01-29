import TrackCard from "@/components/TrackCard";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";

export default function Home() {
  const content = contentData as ContentIndex;
  const { tracks, topics, modules, problems } = content;

  return (
    <div>
      <section className="relative overflow-hidden border-b border-[var(--border-primary)] bg-white">
        <div className="hero-grid absolute inset-0" />
        <div className="relative mx-auto max-w-7xl px-6 py-16">
          <p className="font-mono text-xs uppercase tracking-[0.4em] text-[var(--text-muted)]">
            Code Lab · High-Tech Learning
          </p>
          <h1 className="mt-5 text-4xl font-semibold leading-tight text-[var(--text-primary)] md:text-5xl">
            Master the fundamentals. <span className="gradient-text">Ace the interview.</span>
          </h1>
          <p className="mt-4 max-w-2xl text-lg text-[var(--text-secondary)]">
            Learn concepts, build with code, and practice the exact patterns that
            show up in technical interviews. A premium, focused platform for
            high-velocity learning.
          </p>
          <div className="mt-10 flex flex-wrap gap-4">
            <div className="stat-chip">
              <span className="text-2xl font-semibold">{topics.length}</span>
              <span className="text-xs text-[var(--text-muted)]">Topics</span>
            </div>
            <div className="stat-chip">
              <span className="text-2xl font-semibold">{modules.length}</span>
              <span className="text-xs text-[var(--text-muted)]">Labs</span>
            </div>
            <div className="stat-chip">
              <span className="text-2xl font-semibold">{problems.length}</span>
              <span className="text-xs text-[var(--text-muted)]">Problems</span>
            </div>
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl px-6 py-14">
        <div className="mb-8 flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-semibold">Tracks</h2>
            <p className="mt-2 text-sm text-[var(--text-secondary)]">
              Choose a track to explore curated topics, notes, labs, and practice problems.
            </p>
          </div>
        </div>
        <div className="grid gap-6 md:grid-cols-2 xl:grid-cols-3">
          {tracks.map((track) => (
            <TrackCard key={track.id} {...track} />
          ))}
        </div>
      </section>
    </div>
  );
}
