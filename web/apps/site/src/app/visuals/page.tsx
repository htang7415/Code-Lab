import Link from "next/link";
import GradientDescentViz from "@/components/GradientDescentViz";
import HomeHeroViz from "@/components/HomeHeroViz";
import HomeSoftmaxViz from "@/components/HomeSoftmaxViz";
import HomeSignalViz from "@/components/HomeSignalViz";

export default function VisualsPage() {
  return (
    <div className="visuals-page">
      <section className="visuals-hero">
        <div>
          <div className="visuals-eyebrow">Visual notebooks</div>
          <h1>Interactive demos for learning & sharing.</h1>
          <p>
            These labs are designed to make core ideas tangible. Adjust a slider,
            watch the behavior change, and connect the math to the code.
          </p>
        </div>
        <div className="visuals-hero-cta">
          <Link href="/search" className="home-cta-secondary">
            Explore the library
          </Link>
          <Link
            href="/track/ml/fundamentals"
            className="home-cta-primary"
          >
            Start with fundamentals
          </Link>
        </div>
      </section>

      <section className="visuals-grid">
        <div className="visuals-card" data-parallax="8">
          <HomeHeroViz />
        </div>
        <div className="visuals-card" data-parallax="6">
          <HomeSoftmaxViz />
        </div>
        <div className="visuals-card" data-parallax="6">
          <HomeSignalViz />
        </div>
        <div className="visuals-card" data-parallax="10">
          <GradientDescentViz />
        </div>
      </section>

      <section className="visuals-footer">
        <div>
          <h2>Shareable by default</h2>
          <p>
            Every demo is paired with concise theory and code. Copy it, remix it,
            and build your own visual explanations.
          </p>
        </div>
        <Link href="/search" className="home-section-link">
          Browse all content
        </Link>
      </section>
    </div>
  );
}
