"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import type { SidebarSection } from "@/lib/navigation";
import { useState, useEffect } from "react";

interface SidebarProps {
  sections: SidebarSection[];
}

export default function Sidebar({ sections }: SidebarProps) {
  const pathname = usePathname();
  const [openTracks, setOpenTracks] = useState<Set<string>>(new Set());

  useEffect(() => {
    for (const section of sections) {
      const isActive =
        pathname === `/track/${section.trackId}` ||
        section.items.some((item) => pathname === item.href);
      if (isActive) {
        setOpenTracks((prev) => new Set(prev).add(section.trackId));
        break;
      }
    }
  }, [pathname, sections]);

  function toggle(trackId: string) {
    setOpenTracks((prev) => {
      const next = new Set(prev);
      if (next.has(trackId)) next.delete(trackId);
      else next.add(trackId);
      return next;
    });
  }

  return (
    <aside className="handbook-sidebar">
      <nav className="sidebar-nav">
        {sections.map((section) => {
          const isOpen = openTracks.has(section.trackId);
          return (
            <div key={section.trackId} className="sidebar-section">
              <button
                className="sidebar-track-btn"
                onClick={() => toggle(section.trackId)}
              >
                <svg
                  className={`sidebar-chevron ${isOpen ? "sidebar-chevron-open" : ""}`}
                  width="14"
                  height="14"
                  viewBox="0 0 16 16"
                  fill="none"
                >
                  <path
                    d="M6 4l4 4-4 4"
                    stroke="currentColor"
                    strokeWidth="1.5"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                  />
                </svg>
                <span
                  className="sidebar-track-dot"
                  style={{ background: `var(${section.accentVar})` }}
                />
                <span className="sidebar-track-name">{section.trackName}</span>
              </button>
              {isOpen && (
                <ul className="sidebar-topic-list">
                  {section.items.map((item) => {
                    const isActive = pathname === item.href;
                    return (
                      <li key={item.topicId}>
                        <Link
                          href={item.href}
                          className={`sidebar-topic-link ${isActive ? "sidebar-topic-active" : ""}`}
                        >
                          {item.topicName}
                        </Link>
                      </li>
                    );
                  })}
                </ul>
              )}
            </div>
          );
        })}
      </nav>
    </aside>
  );
}
