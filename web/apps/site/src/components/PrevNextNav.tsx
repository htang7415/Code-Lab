import Link from "next/link";
import type { NavItem } from "@/lib/navigation";

interface PrevNextNavProps {
  prev: NavItem | null;
  next: NavItem | null;
}

export default function PrevNextNav({ prev, next }: PrevNextNavProps) {
  if (!prev && !next) return null;

  return (
    <nav className="prev-next-nav">
      {prev ? (
        <Link
          href={prev.href}
          className="prev-next-link prev-next-prev"
          data-parallax="6"
        >
          <span className="prev-next-label">&larr; Previous</span>
          <span className="prev-next-title">{prev.topicName}</span>
        </Link>
      ) : (
        <span />
      )}
      {next ? (
        <Link
          href={next.href}
          className="prev-next-link prev-next-next"
          data-parallax="6"
        >
          <span className="prev-next-label">Next &rarr;</span>
          <span className="prev-next-title">{next.topicName}</span>
        </Link>
      ) : (
        <span />
      )}
    </nav>
  );
}
