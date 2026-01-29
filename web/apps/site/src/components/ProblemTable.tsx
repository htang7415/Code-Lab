interface Problem {
  id: string;
  slug: string;
  title: string;
  track: string;
  topic: string;
  difficulty: string;
  tags: string[];
  languages: string[];
  summary?: string;
}

const difficultyClass: Record<string, string> = {
  easy: "text-[var(--easy)] bg-green-500/10",
  medium: "text-[var(--medium)] bg-yellow-500/10",
  hard: "text-[var(--hard)] bg-red-500/10",
};

interface ProblemTableProps {
  problems: Problem[];
}

export default function ProblemTable({ problems }: ProblemTableProps) {
  if (problems.length === 0) {
    return (
      <div className="surface-card p-6 text-center text-sm text-[var(--text-muted)]">
        No problems yet. Add problems to see them here.
      </div>
    );
  }

  return (
    <div className="table-surface">
      <table>
        <thead>
          <tr>
            <th>Title</th>
            <th>Track</th>
            <th>Topic</th>
            <th>Difficulty</th>
            <th>Tags</th>
          </tr>
        </thead>
        <tbody>
          {problems.map((problem) => (
            <tr key={problem.id} className="table-row">
              <td>
                <div className="text-sm font-medium text-[var(--text-primary)]">
                  {problem.title}
                </div>
                {problem.summary && (
                  <p className="mt-1 text-xs text-[var(--text-muted)]">
                    {problem.summary}
                  </p>
                )}
              </td>
              <td className="text-xs text-[var(--text-secondary)]">
                {problem.track}
              </td>
              <td className="text-xs text-[var(--text-secondary)]">
                {problem.topic}
              </td>
              <td>
                <span
                  className={`inline-flex rounded-full px-2.5 py-0.5 text-xs font-semibold ${
                    difficultyClass[problem.difficulty] ||
                    "text-[var(--text-muted)] bg-slate-500/10"
                  }`}
                >
                  {problem.difficulty}
                </span>
              </td>
              <td>
                {problem.tags.length === 0 ? (
                  <span className="text-xs text-[var(--text-muted)]">—</span>
                ) : (
                  <div className="flex flex-wrap gap-2">
                    {problem.tags.map((tag) => (
                      <span key={tag} className="badge font-mono">
                        {tag}
                      </span>
                    ))}
                  </div>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
