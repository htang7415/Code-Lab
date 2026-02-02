import hljs from "highlight.js";
import CopyButton from "./CopyButton";

const LANGUAGE_ALIASES: Record<string, string> = {
  js: "javascript",
  ts: "typescript",
  tsx: "typescript",
  jsx: "javascript",
  py: "python",
  rs: "rust",
  md: "markdown",
  yml: "yaml",
  sh: "bash",
  text: "plaintext",
};

interface CodeBlockProps {
  language: string;
  code: string;
}

export default function CodeBlock({ language, code }: CodeBlockProps) {
  const normalizedLanguage = LANGUAGE_ALIASES[language] ?? language;
  const highlighted = hljs.getLanguage(normalizedLanguage)
    ? hljs.highlight(code, { language: normalizedLanguage }).value
    : hljs.highlightAuto(code).value;

  return (
    <div className="code-block">
      <div className="code-block-header">
        <div className="flex items-center gap-2.5">
          <span className="code-block-lang">{language}</span>
          <CopyButton text={code} />
        </div>
      </div>
      <pre>
        <code
          className={`hljs language-${normalizedLanguage}`}
          dangerouslySetInnerHTML={{ __html: highlighted }}
        />
      </pre>
    </div>
  );
}
