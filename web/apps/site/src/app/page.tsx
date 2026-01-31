import Link from "next/link";
import type { ContentIndex } from "@/lib/content";
import contentData from "@/content/content_index.json";
import { sortTracks, sortTopicsForTrack } from "@/lib/roadmap";
import HomeHeroViz from "@/components/HomeHeroViz";
import HomeSoftmaxViz from "@/components/HomeSoftmaxViz";
import HomeSignalViz from "@/components/HomeSignalViz";

export default function Home() {
  const content = contentData as ContentIndex;
  const tracks = sortTracks(content.tracks);
  const topics = content.topics;
  const { modules } = content;
  const primaryTrack = tracks[0];

  return (
    <div className="home-page">
      <section className="home-hero">
        <div className="home-hero-text">
          <div className="home-eyebrow">Open knowledge • Visual labs • Shareable code</div>
          <h1 className="home-title">
            Learn fundamentals through visual, executable ideas.
          </h1>
          <p className="home-lede">
            Code Lab turns every concept into a shared artifact: clear theory,
            minimal math, and runnable demos you can remix. Built for learners
            and educators alike.
          </p>
          <div className="home-cta">
            {primaryTrack ? (
              <Link
                href={`/track/${primaryTrack.id}`}
                className="home-cta-primary"
              >
                Start with {primaryTrack.name}
              </Link>
            ) : null}
            <Link href="/search" className="home-cta-secondary">
              Explore the library
            </Link>
          </div>
          <div className="home-metrics">
            <div className="home-metric">
              <span className="home-metric-label">Tracks</span>
              <span className="home-metric-value">{tracks.length}</span>
            </div>
            <div className="home-metric">
              <span className="home-metric-label">Topics</span>
              <span className="home-metric-value">{topics.length}</span>
            </div>
            <div className="home-metric">
              <span className="home-metric-label">Demos</span>
              <span className="home-metric-value">{modules.length}</span>
            </div>
          </div>
        </div>
        <div className="home-hero-viz">
          <HomeHeroViz />
        </div>
      </section>

      <section className="home-lab-grid">
        <div className="home-lab-intro">
          <h2>Interactive mini-labs</h2>
          <p>LLM-focused previews: attention, token probabilities, and encodings.</p>
        </div>
        <div className="home-lab-cards">
          <HomeSoftmaxViz />
          <HomeSignalViz />
        </div>
      </section>

      <section className="home-feature-grid">
        <div className="home-feature-card" data-parallax="6">
          <div className="home-feature-icon">◆</div>
          <h3>Concept → Math → Code</h3>
          <p>
            Each topic ships with a compact theory note, the core equations, and
            runnable demo code so you can connect intuition to implementation.
          </p>
        </div>
        <div className="home-feature-card" data-parallax="6">
          <div className="home-feature-icon">◈</div>
          <h3>Interactive by design</h3>
          <p>
            Live sliders, plotted signals, and step-by-step visuals powered by
            D3 + Observable. See the behavior, not just the result.
          </p>
        </div>
        <div className="home-feature-card" data-parallax="6">
          <div className="home-feature-icon">◎</div>
          <h3>Fast, focused learning</h3>
          <p>
            Modules stay small and testable so you can build mental models one
            idea at a time—and share them without friction.
          </p>
        </div>
      </section>

      <section className="home-share">
        <div className="home-share-card" data-parallax="8">
          <div className="home-share-header">
            <div>
              <h3>Knowledge & code for everyone</h3>
              <p>Open notes, readable math, and demos you can remix.</p>
            </div>
            <Link href="/search" className="home-share-link">
              Browse demos
            </Link>
          </div>
          <div className="home-share-grid">
            <div className="home-share-item">
              <span>Notes</span>
              <p>Concise, concept-first explanations built for quick recall.</p>
            </div>
            <div className="home-share-item">
              <span>Code</span>
              <p>Runnable snippets with tiny tests so you can experiment safely.</p>
            </div>
            <div className="home-share-item">
              <span>Community</span>
              <p>Copy, remix, and contribute—each module is designed to evolve.</p>
            </div>
          </div>
        </div>
      </section>

      <section className="home-tracks">
        <div className="home-section-header">
          <div>
            <h2>Tracks</h2>
            <p>Choose a domain and explore the visual labs.</p>
          </div>
          <Link href="/search" className="home-section-link">
            View everything
          </Link>
        </div>

        <div className="home-track-stack">
          {tracks.map((track) => {
            const trackTopics = sortTopicsForTrack(
              topics.filter((t) => t.track === track.id),
              track.id
            );

            return (
              <section key={track.id} className="track-section" data-parallax="10">
                <div className="track-section-header">
                  <span
                    className="track-section-dot"
                    style={{ background: `var(${track.accentVar})` }}
                  />
                  <Link
                    href={`/track/${track.id}`}
                    className="text-[0.92rem] font-semibold tracking-tight hover:text-[var(--accent)]"
                  >
                    {track.name}
                  </Link>
                  <span className="track-section-count">
                    {trackTopics.length} topics
                  </span>
                </div>
                <p className="text-[0.8rem] text-[var(--text-muted)] mb-1">
                  {track.description}
                </p>
                <div className="track-topic-grid">
                  {trackTopics.map((topic) => (
                    <Link
                      key={topic.topic}
                      href={`/track/${track.id}/${topic.topic}`}
                      className="track-topic-link"
                    >
                      {topic.name}
                    </Link>
                  ))}
                </div>
              </section>
            );
          })}
        </div>
      </section>
    </div>
  );
}
