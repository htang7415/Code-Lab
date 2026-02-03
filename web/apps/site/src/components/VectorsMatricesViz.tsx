"use client";

import { useMemo, useState } from "react";

const GRID_EXTENT = 2;
const VIEW_EXTENT = 4;

function formatValue(value: number) {
  return value.toFixed(2);
}

function SliderControl({
  label,
  value,
  onChange,
  min = -2,
  max = 2,
  step = 0.1,
}: {
  label: string;
  value: number;
  onChange: (value: number) => void;
  min?: number;
  max?: number;
  step?: number;
}) {
  return (
    <label className="observable-control">
      <span className="observable-control-label">{label}</span>
      <input
        className="observable-control-input"
        type="range"
        min={min}
        max={max}
        step={step}
        value={value}
        onChange={(event) => onChange(Number(event.target.value))}
      />
      <span className="observable-control-value">{formatValue(value)}</span>
    </label>
  );
}

export default function VectorsMatricesViz() {
  const [a, setA] = useState(1);
  const [b, setB] = useState(0);
  const [c, setC] = useState(0);
  const [d, setD] = useState(1);
  const [x1, setX1] = useState(1);
  const [x2, setX2] = useState(0.5);

  const gridLines = useMemo(() => {
    const lines: Array<{ x1: number; y1: number; x2: number; y2: number }> = [];
    for (let i = -GRID_EXTENT; i <= GRID_EXTENT; i += 1) {
      lines.push({ x1: -GRID_EXTENT, y1: i, x2: GRID_EXTENT, y2: i });
      lines.push({ x1: i, y1: -GRID_EXTENT, x2: i, y2: GRID_EXTENT });
    }
    return lines;
  }, []);

  const transform = (x: number, y: number) => ({
    x: a * x + b * y,
    y: c * x + d * y,
  });

  const transformedVector = transform(x1, x2);
  const det = a * d - b * c;

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Matrix Transform Explorer</div>
        <p className="observable-viz-subtitle">
          Adjust the matrix and vector to see how A transforms points and vectors
          in 2D.
        </p>
      </div>

      <div className="observable-controls">
        <SliderControl label="a (row 1, col 1)" value={a} onChange={setA} />
        <SliderControl label="b (row 1, col 2)" value={b} onChange={setB} />
        <SliderControl label="c (row 2, col 1)" value={c} onChange={setC} />
        <SliderControl label="d (row 2, col 2)" value={d} onChange={setD} />
        <SliderControl label="x₁ (vector x)" value={x1} onChange={setX1} min={-2} max={2} />
        <SliderControl label="x₂ (vector y)" value={x2} onChange={setX2} min={-2} max={2} />
      </div>

      <div className="observable-chart">
        <svg
          viewBox={`${-VIEW_EXTENT} ${-VIEW_EXTENT} ${VIEW_EXTENT * 2} ${VIEW_EXTENT * 2}`}
          className="observable-chart-svg matrix-viz"
          role="img"
          aria-label="Matrix transform visualization"
        >
          <defs>
            <marker
              id="arrow-original"
              viewBox="0 0 10 10"
              refX="6"
              refY="5"
              markerWidth="5"
              markerHeight="5"
              orient="auto-start-reverse"
            >
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#0ea5e9" />
            </marker>
            <marker
              id="arrow-transformed"
              viewBox="0 0 10 10"
              refX="6"
              refY="5"
              markerWidth="5"
              markerHeight="5"
              orient="auto-start-reverse"
            >
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#f97316" />
            </marker>
          </defs>

          <rect
            x={-VIEW_EXTENT}
            y={-VIEW_EXTENT}
            width={VIEW_EXTENT * 2}
            height={VIEW_EXTENT * 2}
            className="matrix-bg"
          />

          <g transform="scale(1,-1)">
            <g className="matrix-grid-original">
              {gridLines.map((line, index) => (
                <line
                  key={`grid-${index}`}
                  x1={line.x1}
                  y1={line.y1}
                  x2={line.x2}
                  y2={line.y2}
                />
              ))}
            </g>
            <g className="matrix-grid-transformed">
              {gridLines.map((line, index) => {
                const p1 = transform(line.x1, line.y1);
                const p2 = transform(line.x2, line.y2);
                return (
                  <line
                    key={`tgrid-${index}`}
                    x1={p1.x}
                    y1={p1.y}
                    x2={p2.x}
                    y2={p2.y}
                  />
                );
              })}
            </g>
            <g className="matrix-axes">
              <line x1={-VIEW_EXTENT} y1={0} x2={VIEW_EXTENT} y2={0} />
              <line x1={0} y1={-VIEW_EXTENT} x2={0} y2={VIEW_EXTENT} />
            </g>
            <g className="matrix-vectors">
              <line
                x1={0}
                y1={0}
                x2={x1}
                y2={x2}
                className="matrix-vector-original"
                markerEnd="url(#arrow-original)"
              />
              <line
                x1={0}
                y1={0}
                x2={transformedVector.x}
                y2={transformedVector.y}
                className="matrix-vector-transformed"
                markerEnd="url(#arrow-transformed)"
              />
            </g>
          </g>
        </svg>
      </div>

      <div className="observable-stats">
        <div className="observable-stat-row">
          <span>A</span>
          <span className="observable-stat-value">
            [[{formatValue(a)}, {formatValue(b)}], [{formatValue(c)}, {formatValue(d)}]]
          </span>
        </div>
        <div className="observable-stat-row">
          <span>x</span>
          <span className="observable-stat-value">
            [{formatValue(x1)}, {formatValue(x2)}]
          </span>
        </div>
        <div className="observable-stat-row">
          <span>A x</span>
          <span className="observable-stat-value">
            [{formatValue(transformedVector.x)}, {formatValue(transformedVector.y)}]
          </span>
        </div>
        <div className="observable-stat-row">
          <span>det(A)</span>
          <span className="observable-stat-value">{formatValue(det)}</span>
        </div>
      </div>
    </div>
  );
}
