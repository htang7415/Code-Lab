export interface Track {
  id: string;
  name: string;
  description: string;
  accent: string;
  accentVar: string;
  topicCount: number;
  moduleCount: number;
  problemCount: number;
}

export interface Topic {
  track: string;
  topic: string;
  name: string;
  path: string;
  hasDoc: boolean;
  docCount: number;
  moduleCount: number;
  problemCount: number;
}

export interface ModuleSource {
  path: string;
  language: string;
  content: string;
}

export interface ModuleEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  readme: string;
  sources: ModuleSource[];
}

export interface ProblemEntry {
  id: string;
  slug: string;
  title: string;
  track: string;
  topic: string;
  difficulty: string;
  tags: string[];
  languages: string[];
  path: string;
  summary?: string;
  statement: string;
}

export interface DocEntry {
  track: string;
  topic: string;
  slug: string;
  title: string;
  path: string;
  summary?: string;
  content: string;
}

export interface ContentIndex {
  generated_at: string;
  tracks: Track[];
  topics: Topic[];
  modules: ModuleEntry[];
  problems: ProblemEntry[];
  docs: DocEntry[];
}
