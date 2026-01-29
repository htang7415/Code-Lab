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

const difficultyColor: Record<string, string> = {
  easy: "#22c55e",
  medium: "#eab308",
  hard: "#ef4444",
};

export default function Home() {
  const problems = problemsIndex as Problem[];

  return (
    <main
      style={{
        maxWidth: 900,
        margin: "0 auto",
        padding: "3rem 1.5rem",
      }}
    >
      <h1 style={{ fontSize: "2.5rem", marginBottom: "0.25rem" }}>Code Lab</h1>
      <p style={{ color: "#888", marginBottom: "2.5rem" }}>
        Practice problems for ML, DSA, AI agents, databases, and software
        engineering.
      </p>

      <h2 style={{ fontSize: "1.25rem", marginBottom: "1rem" }}>Problems</h2>

      {problems.length === 0 ? (
        <p style={{ color: "#666" }}>
          No problems indexed yet. Run{" "}
          <code
            style={{
              background: "#1a1a1a",
              padding: "2px 6px",
              borderRadius: 4,
            }}
          >
            pnpm index
          </code>{" "}
          to generate the index.
        </p>
      ) : (
        <table
          style={{
            width: "100%",
            borderCollapse: "collapse",
          }}
        >
          <thead>
            <tr
              style={{
                borderBottom: "1px solid #333",
                textAlign: "left",
              }}
            >
              <th style={{ padding: "0.75rem 0.5rem" }}>Title</th>
              <th style={{ padding: "0.75rem 0.5rem" }}>Track</th>
              <th style={{ padding: "0.75rem 0.5rem" }}>Topic</th>
              <th style={{ padding: "0.75rem 0.5rem" }}>Difficulty</th>
              <th style={{ padding: "0.75rem 0.5rem" }}>Tags</th>
            </tr>
          </thead>
          <tbody>
            {problems.map((p) => (
              <tr
                key={p.id}
                style={{ borderBottom: "1px solid #222" }}
              >
                <td style={{ padding: "0.75rem 0.5rem" }}>{p.title}</td>
                <td style={{ padding: "0.75rem 0.5rem", color: "#888" }}>
                  {p.track}
                </td>
                <td style={{ padding: "0.75rem 0.5rem", color: "#888" }}>
                  {p.topic}
                </td>
                <td
                  style={{
                    padding: "0.75rem 0.5rem",
                    color: difficultyColor[p.difficulty] || "#888",
                  }}
                >
                  {p.difficulty}
                </td>
                <td style={{ padding: "0.75rem 0.5rem", color: "#666" }}>
                  {p.tags.join(", ")}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </main>
  );
}
