import Link from "next/link";

interface Crumb {
  label: string;
  href?: string;
}

interface BreadcrumbProps {
  items: Crumb[];
}

export default function Breadcrumb({ items }: BreadcrumbProps) {
  return (
    <nav className="flex flex-wrap items-center gap-2 text-xs text-[var(--text-muted)]">
      {items.map((item, index) => (
        <div key={item.label} className="flex items-center gap-2">
          {item.href ? (
            <Link href={item.href} className="nav-pill font-mono">
              {item.label}
            </Link>
          ) : (
            <span className="font-mono text-[var(--text-secondary)]">
              {item.label}
            </span>
          )}
          {index < items.length - 1 && (
            <span className="font-mono text-[var(--text-muted)]">/</span>
          )}
        </div>
      ))}
    </nav>
  );
}
