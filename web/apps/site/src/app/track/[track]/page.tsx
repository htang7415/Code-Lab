import Breadcrumb from "@/components/Breadcrumb";
import TopicCard from "@/components/TopicCard";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { notFound } from "next/navigation";

export function generateStaticParams() {
  const content = contentData as ContentIndex;
  return content.tracks.map((track) => ({ track: track.id }));
}

export default function TrackPage({ params }: { params: { track: string } }) {
  const content = contentData as ContentIndex;
  const track = content.tracks.find((item) => item.id === params.track);
  if (!track) return notFound();

  const topics = content.topics
    .filter((topic) => topic.track === track.id)
    .sort((a, b) => a.name.localeCompare(b.name));

  return (
    <div className="mx-auto max-w-6xl px-6 py-12">
      <div
        className="mb-8 h-1 w-16 rounded-full"
        style={{ background: `var(${track.accentVar})` }}
      />
      <Breadcrumb
        items={[
          { label: "home", href: "/" },
          { label: track.id },
        ]}
      />
      <div className="mt-6">
        <h1 className="text-3xl font-semibold">{track.name}</h1>
        <p className="mt-2 text-sm text-[var(--text-secondary)]">
          {track.description}
        </p>
      </div>
      <div className="mt-10 grid gap-6 md:grid-cols-2 xl:grid-cols-3">
        {topics.map((topic) => (
          <TopicCard
            key={`${topic.track}-${topic.topic}`}
            track={topic.track}
            topic={topic.topic}
            name={topic.name}
            accentVar={track.accentVar}
            hasDoc={topic.hasDoc}
            docCount={topic.docCount}
            moduleCount={topic.moduleCount}
            problemCount={topic.problemCount}
          />
        ))}
      </div>
    </div>
  );
}
