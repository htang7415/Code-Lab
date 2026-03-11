import assert from "node:assert/strict";
import test from "node:test";

import {
  isPaymentRequest,
  parsePaymentRequest,
  validationErrors,
} from "./runtime_validation.ts";

test("validationErrors reports multiple boundary problems", () => {
  assert.deepEqual(validationErrors({ amountCents: 0, currency: "CAD" }), [
    "orderId must be a non-empty string",
    "amountCents must be a positive integer",
    "currency must be USD or EUR",
    "idempotencyKey must be at least 6 characters",
  ]);
});

test("isPaymentRequest narrows validated inputs", () => {
  const input = {
    orderId: "ord_1",
    amountCents: 2500,
    currency: "USD",
    idempotencyKey: "idem-123",
  };

  assert.equal(isPaymentRequest(input), true);
});

test("parsePaymentRequest returns typed data or throws at the boundary", () => {
  const parsed = parsePaymentRequest({
    orderId: "ord_2",
    amountCents: 1800,
    currency: "EUR",
    idempotencyKey: "idem-456",
  });
  assert.equal(parsed.currency, "EUR");

  assert.throws(() => parsePaymentRequest({ orderId: "", amountCents: -1 }));
});
