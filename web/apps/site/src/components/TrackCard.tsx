import Link from "next/link";
import type { CSSProperties } from "react";

interface TrackCardProps {
  id: string;
  name: string;
  description: string;
  accentVar: string;
  topicCount: number;
  moduleCount: number;
  problemCount: number;
}

export default function TrackCard({
  id,
  name,
  description,
  accentVar,
  topicCount,
  moduleCount,
  problemCount,
}: TrackCardProps) {
  const style = { "--accent": `var(${accentVar})` } as CSSProperties;

  return (
    <Link
      href={`/track/${id}`}
      className="gradient-border block h-full p-6"
      style={style}
    >
      <div className="flex items-start justify-between">
        <div>
          <p className="text-xs uppercase tracking-[0.2em] text-[var(--text-muted)]">
            {id}
          </p>
          <h3 className="mt-2 text-xl font-semibold text-[var(--text-primary)]">
            {name}
          </h3>
          <p className="mt-2 text-sm text-[var(--text-secondary)]">
            {description}
          </p>
        </div>
        <div
          className="h-10 w-10 rounded-full"
          style={{
            background: `radial-gradient(circle at 30% 30%, var(${accentVar}), transparent 70%)`,
          }}
        />
      </div>
      <div className="mt-6 flex flex-wrap gap-3 text-xs text-[var(--text-secondary)]">
        <span className="badge">{topicCount} topics</span>
        <span className="badge">{moduleCount} labs</span>
        <span className="badge">{problemCount} problems</span>
      </div>
    </Link>
  );
}
