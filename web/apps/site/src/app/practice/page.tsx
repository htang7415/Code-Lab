import ProblemTable from "@/components/ProblemTable";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";

export default function PracticePage() {
  const content = contentData as ContentIndex;
  const problems = [...content.problems].sort((a, b) => {
    const trackCompare = a.track.localeCompare(b.track);
    if (trackCompare !== 0) return trackCompare;
    const topicCompare = a.topic.localeCompare(b.topic);
    if (topicCompare !== 0) return topicCompare;
    return a.title.localeCompare(b.title);
  });

  return (
    <div className="mx-auto max-w-7xl px-6 py-12">
      <div className="mb-10">
        <p className="font-mono text-xs uppercase tracking-[0.4em] text-[var(--text-muted)]">
          Practice
        </p>
        <h1 className="mt-3 text-3xl font-semibold">Problem Bank</h1>
        <p className="mt-2 text-sm text-[var(--text-secondary)]">
          Focused problem sets to validate your knowledge and interview readiness.
        </p>
      </div>
      <ProblemTable problems={problems} />
    </div>
  );
}
