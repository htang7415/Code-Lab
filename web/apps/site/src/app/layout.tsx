import type { Metadata } from "next";
import Link from "next/link";
import "./globals.css";

export const metadata: Metadata = {
  title: "Code Lab",
  description:
    "A high-tech learning platform for fundamentals, code labs, and interview practice.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen text-[var(--text-primary)] antialiased">
        <header className="border-b border-[var(--border-primary)] bg-[rgba(7,11,18,0.8)] backdrop-blur">
          <div className="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
            <Link
              href="/"
              className="flex items-center gap-3 text-lg font-semibold tracking-tight"
            >
              <span className="font-mono text-[var(--accent)]">&gt;_</span>
              <span>Code Lab</span>
            </Link>
            <nav className="flex items-center gap-3 text-sm">
              <Link href="/" className="nav-pill">
                Learn
              </Link>
              <Link href="/practice" className="nav-pill">
                Practice
              </Link>
            </nav>
          </div>
        </header>
        <main>{children}</main>
      </body>
    </html>
  );
}
