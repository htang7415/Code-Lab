"use client";

import { useMemo, useState } from "react";
import * as d3 from "d3";

const WIDTH = 320;
const HEIGHT = 220;
const MARGIN = { top: 16, right: 16, bottom: 32, left: 28 };

export default function HomeSignalViz() {
  const [scale, setScale] = useState(1.5);

  const pointsSin = useMemo(() => {
    return d3.range(0, Math.PI * 2 + 0.01, 0.1).map((x) => ({
      x,
      y: Math.sin(scale * x),
    }));
  }, [scale]);

  const pointsCos = useMemo(() => {
    return d3.range(0, Math.PI * 2 + 0.01, 0.1).map((x) => ({
      x,
      y: Math.cos(scale * x),
    }));
  }, [scale]);

  const xScale = useMemo(
    () =>
      d3
        .scaleLinear()
        .domain([0, Math.PI * 2])
        .range([MARGIN.left, WIDTH - MARGIN.right]),
    []
  );

  const yScale = useMemo(
    () =>
      d3
        .scaleLinear()
        .domain([-1.2, 1.2])
        .range([HEIGHT - MARGIN.bottom, MARGIN.top]),
    []
  );

  const line = useMemo(
    () =>
      d3
        .line<{ x: number; y: number }>()
        .x((d) => xScale(d.x))
        .y((d) => yScale(d.y))
        .curve(d3.curveCatmullRom.alpha(0.5)),
    [xScale, yScale]
  );

  return (
    <div className="home-lab-card" data-parallax="6">
      <div className="home-lab-header">
        <div>
          <div className="home-lab-title">Positional encoding</div>
          <div className="home-lab-meta">Sinusoidal signals</div>
        </div>
        <span className="home-lab-pill">LLM</span>
      </div>
      <div className="home-lab-chart">
        <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} role="img" aria-label="Signal preview">
          <line
            className="home-lab-baseline"
            x1={MARGIN.left}
            x2={WIDTH - MARGIN.right}
            y1={yScale(0)}
            y2={yScale(0)}
          />
          <path className="home-lab-line" d={line(pointsSin) ?? ""} />
          <path className="home-lab-line-alt" d={line(pointsCos) ?? ""} />
        </svg>
      </div>
      <label className="home-lab-control">
        <span>Scale</span>
        <input
          type="range"
          min="0.6"
          max="3"
          step="0.1"
          value={scale}
          onChange={(event) => setScale(parseFloat(event.target.value))}
        />
        <strong>{scale.toFixed(1)}</strong>
      </label>
    </div>
  );
}
