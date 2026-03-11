import assert from "node:assert/strict";
import test from "node:test";

import {
  schemaVersionsCompatible,
  shouldShareType,
  toUserCard,
} from "./frontend_backend_shared_types.ts";

test("toUserCard projects a narrower UI-facing shape", () => {
  assert.deepEqual(
    toUserCard({
      id: "u_1",
      displayName: "Alex",
      role: "admin",
      version: 2,
    }),
    {
      id: "u_1",
      label: "Alex",
      canManage: true,
    },
  );
});

test("schemaVersionsCompatible keeps version mismatches explicit", () => {
  assert.equal(schemaVersionsCompatible(2, 2), true);
  assert.equal(schemaVersionsCompatible(2, 3), false);
});

test("shouldShareType prefers stable, multi-consumer contracts", () => {
  assert.equal(shouldShareType(3, 1), true);
  assert.equal(shouldShareType(1, 0), false);
  assert.equal(shouldShareType(3, 2), false);
});
