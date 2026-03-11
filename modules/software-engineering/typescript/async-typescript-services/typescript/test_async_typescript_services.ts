import assert from "node:assert/strict";
import test from "node:test";

import {
  callWithBudget,
  concurrencyBudget,
  deadlineRemaining,
  shouldRetry,
} from "./async_typescript_services.ts";

test("concurrencyBudget and deadlineRemaining keep service limits explicit", () => {
  assert.equal(concurrencyBudget(4, 8), 32);
  assert.equal(deadlineRemaining(250, 90), 160);
  assert.equal(deadlineRemaining(100, 140), 0);
});

test("callWithBudget rejects excess in-flight work before starting the task", async () => {
  let started = false;
  const result = await callWithBudget(8, 8, async () => {
    started = true;
    return "unexpected";
  });

  assert.deepEqual(result, { ok: false, retryable: true, reason: "backpressure" });
  assert.equal(shouldRetry(result), true);
  assert.equal(started, false);
});

test("callWithBudget captures typed success and failure shapes", async () => {
  const ok = await callWithBudget(1, 4, async () => "done");
  assert.deepEqual(ok, { ok: true, value: "done" });

  const failed = await callWithBudget(1, 4, async () => {
    throw new Error("boom");
  });
  assert.deepEqual(failed, { ok: false, retryable: false, reason: "boom" });
});
