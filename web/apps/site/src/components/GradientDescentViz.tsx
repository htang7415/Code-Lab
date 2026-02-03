"use client";

import { useEffect, useRef } from "react";
import { Runtime, Inspector } from "@observablehq/runtime";
import define from "@/observable/gradientDescent";

export default function GradientDescentViz() {
  const controlsRef = useRef<HTMLDivElement>(null);
  const chartRef = useRef<HTMLDivElement>(null);
  const statsRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const controls = controlsRef.current;
    const chart = chartRef.current;
    const stats = statsRef.current;
    if (!controls || !chart || !stats) return;

    controls.innerHTML = "";
    chart.innerHTML = "";
    stats.innerHTML = "";

    const runtime = new Runtime();
    runtime.module(define, (name: string) => {
      if (name === "viewof lr") return new Inspector(controls);
      if (name === "viewof steps") return new Inspector(controls);
      if (name === "viewof x0") return new Inspector(controls);
      if (name === "chart") return new Inspector(chart);
      if (name === "stats") return new Inspector(stats);
      return undefined;
    });

    return () => runtime.dispose();
  }, []);

  return (
    <div className="observable-viz">
      <div className="observable-viz-header">
        <div className="observable-viz-title">Gradient Descent Playground</div>
        <p className="observable-viz-subtitle">
          Adjust the learning rate, steps, and starting point to see how updates
          move along a quadratic curve.
        </p>
      </div>
      <div ref={controlsRef} className="observable-controls" />
      <div ref={chartRef} className="observable-chart" />
      <div ref={statsRef} />
    </div>
  );
}
