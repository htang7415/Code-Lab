import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { sortTopicsForTrack } from "@/lib/roadmap";
import { notFound } from "next/navigation";

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.tracks.map((track) => ({ track: track.id }));
}

export default async function TrackPage({ params }: { params: Promise<{ track: string }> }) {
  const { track: trackId } = await params;
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === trackId);
  if (!track) return notFound();

  const topics = sortTopicsForTrack(
    content.topics.filter((topic) => topic.track === track.id),
    track.id
  );

  return (
    <div>
      <div className="flex items-center gap-2.5 mb-1">
        <span
          className="h-2.5 w-2.5 rounded-full"
          style={{ background: `var(${track.accentVar})` }}
        />
        <span className="text-[0.72rem] font-semibold uppercase tracking-widest text-[var(--text-muted)]">
          Track
        </span>
      </div>
      <h1 className="text-2xl font-semibold tracking-tight">{track.name}</h1>
      <p className="mt-1.5 text-[0.88rem] text-[var(--text-secondary)] max-w-lg">
        {track.description}
      </p>
      <p className="mt-2 text-[0.75rem] text-[var(--text-muted)]">
        {topics.length} topics
      </p>

      <div className="mt-6 space-y-0.5">
        {topics.map((topic) => {
          const entryCount = topic.docCount + topic.moduleCount;
          return (
            <Link
              key={topic.topic}
              href={`/track/${track.id}/${topic.topic}`}
              className="topic-list-item"
              data-parallax="4"
            >
              <span
                className="topic-list-dot"
                style={{ background: `var(${track.accentVar})` }}
              />
              <span className="topic-list-name">{topic.name}</span>
              {entryCount > 0 && (
                <span className="topic-list-meta">
                  {entryCount} {entryCount === 1 ? "entry" : "entries"}
                </span>
              )}
            </Link>
          );
        })}
      </div>
    </div>
  );
}
