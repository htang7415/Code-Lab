import Link from "next/link";
import type { CSSProperties } from "react";

interface TopicCardProps {
  track: string;
  topic: string;
  name: string;
  accentVar: string;
  hasDoc: boolean;
  docCount: number;
  moduleCount: number;
  problemCount: number;
}

export default function TopicCard({
  track,
  topic,
  name,
  accentVar,
  hasDoc,
  docCount,
  moduleCount,
  problemCount,
}: TopicCardProps) {
  const isEmpty = !hasDoc && moduleCount === 0 && problemCount === 0;
  const style = { "--accent": `var(${accentVar})` } as CSSProperties;

  return (
    <Link
      href={`/track/${track}/${topic}`}
      className={`gradient-border block p-5 transition-opacity ${
        isEmpty ? "opacity-60" : "opacity-100"
      }`}
      style={style}
    >
      <div className="flex items-center justify-between">
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-[var(--text-muted)]">
            {topic}
          </p>
          <h3 className="mt-2 text-lg font-semibold text-[var(--text-primary)]">
            {name}
          </h3>
        </div>
        <div
          className="h-9 w-9 rounded-full"
          style={{
            background: `radial-gradient(circle at 30% 30%, var(${accentVar}), transparent 70%)`,
          }}
        />
      </div>
      <div className="mt-4 flex flex-wrap gap-2 text-xs text-[var(--text-secondary)]">
        <span className="badge">{docCount} notes</span>
        <span className="badge">{moduleCount} labs</span>
        <span className="badge">{problemCount} problems</span>
      </div>
      {isEmpty && (
        <p className="mt-3 text-xs text-[var(--text-muted)]">
          Content coming soon.
        </p>
      )}
    </Link>
  );
}
