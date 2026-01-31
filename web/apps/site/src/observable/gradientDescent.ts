import * as d3 from "d3";
import type { Runtime } from "@observablehq/runtime";

type Observer = (name: string) => unknown;

interface SliderConfig {
  label: string;
  min: number;
  max: number;
  step: number;
  value: number;
}

interface Point {
  i: number;
  x: number;
  y: number;
}

function slider(config: SliderConfig) {
  const { label, min, max, step, value } = config;
  const form = document.createElement("form") as HTMLFormElement & {
    value: number;
  };
  form.className = "observable-control";
  form.onsubmit = (event) => event.preventDefault();

  const labelEl = document.createElement("span");
  labelEl.className = "observable-control-label";
  labelEl.textContent = label;

  const input = document.createElement("input");
  input.className = "observable-control-input";
  input.type = "range";
  input.min = String(min);
  input.max = String(max);
  input.step = String(step);
  input.value = String(value);

  const valueEl = document.createElement("span");
  valueEl.className = "observable-control-value";
  valueEl.textContent = String(value);

  form.value = value;
  input.addEventListener("input", () => {
    form.value = parseFloat(input.value);
    valueEl.textContent = input.value;
    form.dispatchEvent(new Event("input", { bubbles: true }));
  });

  form.append(labelEl, input, valueEl);
  return form;
}

function statRow(label: string, value: string) {
  const row = document.createElement("div");
  row.className = "observable-stat-row";

  const labelEl = document.createElement("span");
  labelEl.className = "observable-stat-label";
  labelEl.textContent = label;

  const valueEl = document.createElement("span");
  valueEl.className = "observable-stat-value";
  valueEl.textContent = value;

  row.append(labelEl, valueEl);
  return row;
}

export default function define(runtime: Runtime, observer: Observer) {
  const main = runtime.module();

  main
    .variable(observer("viewof lr"))
    .define("viewof lr", () =>
      slider({ label: "Learning rate", min: 0.01, max: 1, step: 0.01, value: 0.2 })
    );
  main
    .variable(observer("lr"))
    .define(
      "lr",
      ["Generators", "viewof lr"],
      (Generators: { input: (element: HTMLElement) => number }, view: HTMLElement) =>
        Generators.input(view)
    );

  main
    .variable(observer("viewof steps"))
    .define("viewof steps", () =>
      slider({ label: "Steps", min: 4, max: 40, step: 1, value: 16 })
    );
  main
    .variable(observer("steps"))
    .define(
      "steps",
      ["Generators", "viewof steps"],
      (Generators: { input: (element: HTMLElement) => number }, view: HTMLElement) =>
        Generators.input(view)
    );

  main
    .variable(observer("viewof x0"))
    .define("viewof x0", () =>
      slider({ label: "Start x", min: -8, max: 8, step: 0.2, value: 6 })
    );
  main
    .variable(observer("x0"))
    .define(
      "x0",
      ["Generators", "viewof x0"],
      (Generators: { input: (element: HTMLElement) => number }, view: HTMLElement) =>
        Generators.input(view)
    );

  main
    .variable(observer("path"))
    .define("path", ["lr", "steps", "x0"], (lr: number, steps: number, x0: number) => {
      const points: Point[] = [];
      let x = x0;
      for (let i = 0; i <= steps; i += 1) {
        points.push({ i, x, y: 0.5 * x * x });
        x = x - lr * x;
      }
      return points;
    });

  main.variable(observer("chart")).define("chart", ["path"], (path: Point[]) => {
    const width = 640;
    const height = 360;
    const margin = { top: 18, right: 18, bottom: 36, left: 46 };

    const domainMax = 8;
    const xScale = d3
      .scaleLinear()
      .domain([-domainMax, domainMax])
      .range([margin.left, width - margin.right]);
    const yMax = 0.5 * domainMax * domainMax;
    const yScale = d3
      .scaleLinear()
      .domain([0, yMax])
      .nice()
      .range([height - margin.bottom, margin.top]);

    const svg = d3
      .create("svg")
      .attr("class", "observable-chart-svg")
      .attr("viewBox", `0 0 ${width} ${height}`)
      .attr("role", "img")
      .attr("aria-label", "Gradient descent path on a quadratic curve");

    const xAxis = d3.axisBottom(xScale).ticks(6).tickSizeOuter(0);
    const yAxis = d3.axisLeft(yScale).ticks(5).tickSizeOuter(0);

    svg
      .append("g")
      .attr("transform", `translate(0,${height - margin.bottom})`)
      .attr("class", "observable-axis")
      .call(xAxis);
    svg
      .append("g")
      .attr("transform", `translate(${margin.left},0)`)
      .attr("class", "observable-axis")
      .call(yAxis);

    const curve = d3.range(-domainMax, domainMax + 0.01, 0.1).map((x) => ({
      x,
      y: 0.5 * x * x,
    }));

    const line = d3
      .line<{ x: number; y: number }>()
      .x((d) => xScale(d.x))
      .y((d) => yScale(d.y));

    svg
      .append("path")
      .datum(curve)
      .attr("class", "observable-curve")
      .attr("d", line);

    svg
      .append("path")
      .datum(path)
      .attr("class", "observable-path")
      .attr("d", line);

    svg
      .append("g")
      .selectAll("circle")
      .data(path)
      .join("circle")
      .attr("class", "observable-point")
      .attr("cx", (d) => xScale(d.x))
      .attr("cy", (d) => yScale(d.y))
      .attr("r", 3);

    const last = path[path.length - 1];
    svg
      .append("circle")
      .attr("class", "observable-point-final")
      .attr("cx", xScale(last.x))
      .attr("cy", yScale(last.y))
      .attr("r", 4.5);

    return svg.node();
  });

  main.variable(observer("stats")).define("stats", ["path"], (path: Point[]) => {
    const last = path[path.length - 1];
    const container = document.createElement("div");
    container.className = "observable-stats";

    container.append(
      statRow("Final x", last.x.toFixed(4)),
      statRow("Final loss", last.y.toFixed(4)),
      statRow("Iterations", String(path.length - 1))
    );

    return container;
  });

  return main;
}
