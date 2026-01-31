import type { ContentIndex, Track, Topic } from "./content";

export interface NavItem {
  trackId: string;
  trackName: string;
  topicId: string;
  topicName: string;
  href: string;
  accentVar: string;
}

export interface SidebarSection {
  trackId: string;
  trackName: string;
  accentVar: string;
  items: { topicId: string; topicName: string; href: string }[];
}

export interface AdjacentPages {
  prev: NavItem | null;
  next: NavItem | null;
}

export function buildNavItems(content: ContentIndex): NavItem[] {
  const trackMap = new Map<string, Track>();
  for (const track of content.tracks) {
    trackMap.set(track.id, track);
  }

  return content.topics
    .slice()
    .sort((a, b) => {
      const trackOrder =
        content.tracks.findIndex((t) => t.id === a.track) -
        content.tracks.findIndex((t) => t.id === b.track);
      if (trackOrder !== 0) return trackOrder;
      return a.name.localeCompare(b.name);
    })
    .map((topic) => {
      const track = trackMap.get(topic.track)!;
      return {
        trackId: track.id,
        trackName: track.name,
        topicId: topic.topic,
        topicName: topic.name,
        href: `/track/${track.id}/${topic.topic}`,
        accentVar: track.accentVar,
      };
    });
}

export function buildSidebarSections(navItems: NavItem[]): SidebarSection[] {
  const sections: SidebarSection[] = [];
  let current: SidebarSection | null = null;

  for (const item of navItems) {
    if (!current || current.trackId !== item.trackId) {
      current = {
        trackId: item.trackId,
        trackName: item.trackName,
        accentVar: item.accentVar,
        items: [],
      };
      sections.push(current);
    }
    current.items.push({
      topicId: item.topicId,
      topicName: item.topicName,
      href: item.href,
    });
  }

  return sections;
}

export function getAdjacentPages(
  navItems: NavItem[],
  trackId: string,
  topicId: string
): AdjacentPages {
  const index = navItems.findIndex(
    (item) => item.trackId === trackId && item.topicId === topicId
  );
  return {
    prev: index > 0 ? navItems[index - 1] : null,
    next: index >= 0 && index < navItems.length - 1 ? navItems[index + 1] : null,
  };
}
