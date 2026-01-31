import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import { buildNavItems, buildSidebarSections } from "@/lib/navigation";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";

export const metadata: Metadata = {
  title: "Code Lab",
  description:
    "A handbook-style learning platform for fundamentals and code labs.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const content = contentData as ContentIndex;
  const navItems = buildNavItems(content);
  const sections = buildSidebarSections(navItems);

  return (
    <html lang="en">
      <body>
        <header className="site-header">
          <div className="site-header-inner">
            <Link href="/" className="header-logo">
              <span className="header-logo-icon">&gt;_</span>
              <span>Code Lab</span>
            </Link>
            <span className="header-tagline">
              Concepts &middot; Code &middot; Mastery
            </span>
          </div>
        </header>
        <div className="handbook-shell">
          <Sidebar sections={sections} />
          <main className="handbook-main">{children}</main>
        </div>
      </body>
    </html>
  );
}
