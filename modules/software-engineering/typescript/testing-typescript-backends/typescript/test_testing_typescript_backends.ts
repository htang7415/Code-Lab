import assert from "node:assert/strict";
import test from "node:test";

import {
  fakeRepository,
  handlerReadyForUnitTest,
  recommendedTestLayers,
} from "./testing_typescript_backends.ts";

test("recommendedTestLayers follows real backend boundaries", () => {
  assert.deepEqual(
    recommendedTestLayers({
      hasDatabase: true,
      hasExternalHttp: true,
      pureDecisionSteps: 2,
    }),
    ["unit", "integration", "contract"],
  );
});

test("fakeRepository supports deterministic handler tests", () => {
  const repo = fakeRepository([
    { id: "u1", name: "Ada" },
    { id: "u2", name: "Lin" },
  ]);

  assert.deepEqual(repo.getById("u1"), { id: "u1", name: "Ada" });
  assert.deepEqual(repo.list(), [
    { id: "u1", name: "Ada" },
    { id: "u2", name: "Lin" },
  ]);
});

test("handlerReadyForUnitTest requires explicit seams", () => {
  assert.equal(handlerReadyForUnitTest(true, 0), true);
  assert.equal(handlerReadyForUnitTest(false, 0), false);
  assert.equal(handlerReadyForUnitTest(true, 1), false);
});
