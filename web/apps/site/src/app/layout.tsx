import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Code Lab",
  description:
    "Practice problems and concept labs for ML, DSA, AI agents, databases, and software engineering",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[var(--bg-primary)] text-[var(--text-primary)] antialiased">
        <header className="border-b border-[var(--border-primary)] bg-[var(--bg-secondary)]">
          <div className="mx-auto flex max-w-5xl items-center justify-between px-6 py-4">
            <a
              href="/"
              className="flex items-center gap-2 text-lg font-semibold tracking-tight"
            >
              <span className="font-mono text-[var(--accent)]">&gt;_</span>
              <span>Code Lab</span>
            </a>
            <nav className="flex items-center gap-6 text-sm text-[var(--text-secondary)]">
              <a
                href="/"
                className="transition-colors hover:text-[var(--text-primary)]"
              >
                Problems
              </a>
            </nav>
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
