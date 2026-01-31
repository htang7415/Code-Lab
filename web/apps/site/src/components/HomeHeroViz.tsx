"use client";

import { useMemo, useState } from "react";
import * as d3 from "d3";

interface Cell {
  i: number;
  j: number;
  value: number;
  active: boolean;
}

const WIDTH = 520;
const HEIGHT = 300;
const MARGIN = { top: 28, right: 24, bottom: 28, left: 36 };
const TOKENS = 8;

export default function HomeHeroViz() {
  const [queryToken, setQueryToken] = useState(6);
  const [locality, setLocality] = useState(2.4);
  const [temperature, setTemperature] = useState(1.0);

  const cellSize = useMemo(() => {
    const width = WIDTH - MARGIN.left - MARGIN.right;
    const height = HEIGHT - MARGIN.top - MARGIN.bottom;
    return Math.min(width, height) / TOKENS;
  }, []);

  const origin = useMemo(
    () => ({
      x: MARGIN.left,
      y: MARGIN.top,
    }),
    []
  );

  const cells = useMemo(() => {
    const rows: Cell[] = [];
    for (let i = 0; i < TOKENS; i += 1) {
      const scores: number[] = [];
      for (let j = 0; j < TOKENS; j += 1) {
        if (j > i) {
          scores.push(-Infinity);
          continue;
        }
        const distance = i - j;
        const score = -((distance * distance) / (2 * locality * locality)) / temperature;
        scores.push(score);
      }
      const max = Math.max(...scores.filter((v) => Number.isFinite(v)));
      const exps = scores.map((s) => (Number.isFinite(s) ? Math.exp(s - max) : 0));
      const sum = exps.reduce((acc, val) => acc + val, 0) || 1;
      const weights = exps.map((val) => val / sum);
      for (let j = 0; j < TOKENS; j += 1) {
        rows.push({
          i,
          j,
          value: weights[j] ?? 0,
          active: i === queryToken - 1,
        });
      }
    }
    return rows;
  }, [locality, temperature, queryToken]);

  const color = useMemo(
    () => d3.scaleSequential(d3.interpolateBlues).domain([0, 1]),
    []
  );

  return (
    <div className="home-viz" data-parallax="10">
      <div className="home-viz-header">
        <div>
          <div className="home-viz-title">Attention map preview</div>
          <div className="home-viz-meta">LLM self-attention &middot; causal mask</div>
        </div>
        <div className="home-viz-badge">Live</div>
      </div>

      <div className="home-viz-chart">
        <svg
          viewBox={`0 0 ${WIDTH} ${HEIGHT}`}
          role="img"
          aria-label="Attention map preview"
        >
          {cells.map((cell) => {
            const x = origin.x + cell.j * cellSize;
            const y = origin.y + cell.i * cellSize;
            const fill =
              cell.value === 0
                ? "rgba(15, 23, 42, 0.04)"
                : color(cell.value);
            return (
              <rect
                key={`${cell.i}-${cell.j}`}
                className={`home-viz-cell${cell.active ? " home-viz-cell-active" : ""}`}
                x={x}
                y={y}
                width={cellSize}
                height={cellSize}
                rx={4}
                fill={fill}
              />
            );
          })}
          {Array.from({ length: TOKENS }).map((_, idx) => (
            <text
              key={`label-x-${idx}`}
              className="home-viz-label"
              x={origin.x + idx * cellSize + cellSize / 2}
              y={origin.y - 6}
              textAnchor="middle"
            >
              {idx + 1}
            </text>
          ))}
          {Array.from({ length: TOKENS }).map((_, idx) => (
            <text
              key={`label-y-${idx}`}
              className="home-viz-label"
              x={origin.x - 10}
              y={origin.y + idx * cellSize + cellSize / 2 + 4}
              textAnchor="end"
            >
              {idx + 1}
            </text>
          ))}
        </svg>
      </div>

      <div className="home-viz-controls">
        <label className="home-viz-control">
          <span>Query token</span>
          <input
            type="range"
            min="1"
            max={TOKENS}
            step="1"
            value={queryToken}
            onChange={(event) => setQueryToken(parseFloat(event.target.value))}
          />
          <strong>{queryToken}</strong>
        </label>
        <label className="home-viz-control">
          <span>Locality</span>
          <input
            type="range"
            min="1"
            max="4"
            step="0.1"
            value={locality}
            onChange={(event) => setLocality(parseFloat(event.target.value))}
          />
          <strong>{locality.toFixed(1)}</strong>
        </label>
        <label className="home-viz-control">
          <span>Temperature</span>
          <input
            type="range"
            min="0.6"
            max="1.8"
            step="0.05"
            value={temperature}
            onChange={(event) => setTemperature(parseFloat(event.target.value))}
          />
          <strong>{temperature.toFixed(2)}</strong>
        </label>
      </div>
    </div>
  );
}
