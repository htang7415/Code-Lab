import assert from "node:assert/strict";
import test from "node:test";

import {
  applyUserPatch,
  isCompleteUserRecord,
  updatableFields,
  type UserRecord,
} from "./type_driven_api_design.ts";

const user: UserRecord = {
  id: "u_1",
  email: "alex@example.com",
  displayName: "Alex",
  role: "viewer",
  active: true,
};

test("applyUserPatch updates only mutable fields", () => {
  const updated = applyUserPatch(user, { displayName: "A. Lee", active: false });
  assert.deepEqual(updated, {
    id: "u_1",
    email: "alex@example.com",
    displayName: "A. Lee",
    role: "viewer",
    active: false,
  });
});

test("updatableFields exposes only keys present in the patch", () => {
  assert.deepEqual(updatableFields({ role: "editor", active: true }), ["role", "active"]);
});

test("isCompleteUserRecord distinguishes partial and complete payloads", () => {
  assert.equal(isCompleteUserRecord(user), true);
  assert.equal(isCompleteUserRecord({ id: "u_2", email: "missing-fields@example.com" }), false);
});
