"use client";

import { useEffect, useState } from "react";

export interface TocHeading {
  id: string;
  text: string;
  level: number; // 2 or 3
}

interface TableOfContentsProps {
  headings: TocHeading[];
}

export default function TableOfContents({ headings }: TableOfContentsProps) {
  const [activeId, setActiveId] = useState<string>("");

  useEffect(() => {
    if (headings.length === 0) return;

    const observer = new IntersectionObserver(
      (entries) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            setActiveId(entry.target.id);
          }
        }
      },
      { rootMargin: "-80px 0px -60% 0px", threshold: 0.1 }
    );

    for (const heading of headings) {
      const el = document.getElementById(heading.id);
      if (el) observer.observe(el);
    }

    return () => observer.disconnect();
  }, [headings]);

  if (headings.length === 0) return null;

  return (
    <aside className="toc-aside">
      <p className="toc-title">On This Page</p>
      <nav className="toc-nav">
        {headings.map((heading) => (
          <a
            key={heading.id}
            href={`#${heading.id}`}
            className={`toc-link ${heading.level === 3 ? "toc-link-nested" : ""} ${
              activeId === heading.id ? "toc-link-active" : ""
            }`}
          >
            {heading.text}
          </a>
        ))}
      </nav>
    </aside>
  );
}
