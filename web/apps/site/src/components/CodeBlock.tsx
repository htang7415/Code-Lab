interface CodeBlockProps {
  filename: string;
  language: string;
  code: string;
}

export default function CodeBlock({ filename, language, code }: CodeBlockProps) {
  return (
    <div className="code-block">
      <div className="code-block-header">
        <span className="font-mono">{filename}</span>
        <span className="font-mono text-xs text-[var(--text-muted)]">
          {language}
        </span>
      </div>
      <pre>
        <code className={`language-${language}`}>{code}</code>
      </pre>
    </div>
  );
}
