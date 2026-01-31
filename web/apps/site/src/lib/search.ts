export interface SearchEntry {
  id: string;
  type: "module" | "doc";
  title: string;
  summary?: string;
  track: string;
  topic: string;
  slug: string;
  href: string;
  trackName: string;
  topicName: string;
}

export interface SearchIndex {
  generated_at: string;
  entries: SearchEntry[];
}
