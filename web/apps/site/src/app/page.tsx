import problemsIndex from "@/content/problems_index.json";

interface Problem {
  id: string;
  slug: string;
  title: string;
  track: string;
  topic: string;
  difficulty: string;
  tags: string[];
  languages: string[];
}

const difficultyClass: Record<string, string> = {
  easy: "text-[var(--easy)] bg-green-500/10",
  medium: "text-[var(--medium)] bg-yellow-500/10",
  hard: "text-[var(--hard)] bg-red-500/10",
};

export default function Home() {
  const problems = problemsIndex as Problem[];

  return (
    <div className="mx-auto max-w-5xl px-6 py-12">
      <div className="mb-12">
        <h1 className="text-4xl font-bold tracking-tight">Code Lab</h1>
        <p className="mt-2 text-lg text-[var(--text-secondary)]">
          Practice problems for ML, DSA, AI agents, databases, and software
          engineering.
        </p>
      </div>

      <section>
        <h2 className="mb-6 text-xl font-semibold">Problems</h2>

        {problems.length === 0 ? (
          <div className="rounded-lg border border-[var(--border-primary)] bg-[var(--bg-card)] p-8 text-center">
            <p className="text-[var(--text-muted)]">
              No problems indexed yet. Run{" "}
              <code className="rounded bg-[var(--bg-secondary)] px-2 py-1 text-sm text-[var(--accent)]">
                pnpm index
              </code>{" "}
              to generate the index.
            </p>
          </div>
        ) : (
          <div className="overflow-hidden rounded-lg border border-[var(--border-primary)]">
            <table className="w-full">
              <thead>
                <tr className="border-b border-[var(--border-primary)] bg-[var(--bg-secondary)] text-left text-sm text-[var(--text-secondary)]">
                  <th className="px-4 py-3 font-medium">Title</th>
                  <th className="px-4 py-3 font-medium">Track</th>
                  <th className="px-4 py-3 font-medium">Topic</th>
                  <th className="px-4 py-3 font-medium">Difficulty</th>
                  <th className="px-4 py-3 font-medium">Tags</th>
                </tr>
              </thead>
              <tbody>
                {problems.map((p) => (
                  <tr
                    key={p.id}
                    className="border-b border-[var(--border-primary)] last:border-b-0 transition-colors hover:bg-[var(--bg-card)]"
                  >
                    <td className="px-4 py-3 font-medium">{p.title}</td>
                    <td className="px-4 py-3 text-sm text-[var(--text-secondary)]">
                      {p.track}
                    </td>
                    <td className="px-4 py-3 text-sm text-[var(--text-secondary)]">
                      {p.topic}
                    </td>
                    <td className="px-4 py-3">
                      <span
                        className={`inline-block rounded-full px-2.5 py-0.5 text-xs font-medium ${
                          difficultyClass[p.difficulty] ||
                          "text-[var(--text-muted)]"
                        }`}
                      >
                        {p.difficulty}
                      </span>
                    </td>
                    <td className="px-4 py-3">
                      <div className="flex flex-wrap gap-1.5">
                        {p.tags.map((tag) => (
                          <span
                            key={tag}
                            className="rounded border border-[var(--border-primary)] bg-[var(--bg-secondary)] px-2 py-0.5 text-xs text-[var(--text-muted)]"
                          >
                            {tag}
                          </span>
                        ))}
                      </div>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </section>
    </div>
  );
}
