"use client";

import { useMemo, useState } from "react";
import * as d3 from "d3";

const WIDTH = 320;
const HEIGHT = 220;
const MARGIN = { top: 16, right: 16, bottom: 34, left: 28 };
const LOGITS = [2, 1, 0, -1];

export default function HomeSoftmaxViz() {
  const [temp, setTemp] = useState(1.0);

  const { bars } = useMemo(() => {
    const scaled = LOGITS.map((l) => l / temp);
    const max = Math.max(...scaled);
    const exps = scaled.map((l) => Math.exp(l - max));
    const sum = exps.reduce((acc, val) => acc + val, 0);
    const probs = exps.map((val) => val / sum);
    return {
      bars: probs.map((p, i) => ({ label: `x${i + 1}`, value: p })),
    };
  }, [temp]);

  const xScale = useMemo(
    () =>
      d3
        .scaleBand()
        .domain(bars.map((b) => b.label))
        .range([MARGIN.left, WIDTH - MARGIN.right])
        .padding(0.3),
    [bars]
  );

  const yScale = useMemo(
    () =>
      d3
        .scaleLinear()
        .domain([0, 1])
        .range([HEIGHT - MARGIN.bottom, MARGIN.top]),
    []
  );

  const colors = d3.schemeCategory10;

  return (
    <div className="home-lab-card" data-parallax="6">
      <div className="home-lab-header">
        <div>
          <div className="home-lab-title">Next-token distribution</div>
          <div className="home-lab-meta">Softmax temperature</div>
        </div>
        <span className="home-lab-pill">LLM</span>
      </div>
      <div className="home-lab-chart">
        <svg viewBox={`0 0 ${WIDTH} ${HEIGHT}`} role="img" aria-label="Softmax distribution">
          {bars.map((bar, idx) => (
            <rect
              key={bar.label}
              className="home-lab-bar"
              x={xScale(bar.label) ?? 0}
              y={yScale(bar.value)}
              width={xScale.bandwidth()}
              height={HEIGHT - MARGIN.bottom - yScale(bar.value)}
              rx={6}
              fill={colors[idx % colors.length]}
            />
          ))}
          {bars.map((bar) => (
            <text
              key={`${bar.label}-label`}
              className="home-lab-label"
              x={(xScale(bar.label) ?? 0) + xScale.bandwidth() / 2}
              y={HEIGHT - 12}
              textAnchor="middle"
            >
              {bar.label}
            </text>
          ))}
        </svg>
      </div>
      <label className="home-lab-control">
        <span>Temperature</span>
        <input
          type="range"
          min="0.4"
          max="2"
          step="0.05"
          value={temp}
          onChange={(event) => setTemp(parseFloat(event.target.value))}
        />
        <strong>{temp.toFixed(2)}</strong>
      </label>
    </div>
  );
}
