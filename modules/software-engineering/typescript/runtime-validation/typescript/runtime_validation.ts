export interface PaymentRequest {
  orderId: string;
  amountCents: number;
  currency: "USD" | "EUR";
  idempotencyKey: string;
}

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

export function validationErrors(input: unknown): string[] {
  if (!isRecord(input)) {
    return ["input must be an object"];
  }

  const errors: string[] = [];
  if (typeof input.orderId !== "string" || input.orderId.trim().length === 0) {
    errors.push("orderId must be a non-empty string");
  }
  if (
    typeof input.amountCents !== "number" ||
    !Number.isInteger(input.amountCents) ||
    input.amountCents <= 0
  ) {
    errors.push("amountCents must be a positive integer");
  }
  if (input.currency !== "USD" && input.currency !== "EUR") {
    errors.push("currency must be USD or EUR");
  }
  if (
    typeof input.idempotencyKey !== "string" ||
    input.idempotencyKey.trim().length < 6
  ) {
    errors.push("idempotencyKey must be at least 6 characters");
  }
  return errors;
}

export function isPaymentRequest(input: unknown): input is PaymentRequest {
  return validationErrors(input).length === 0;
}

export function parsePaymentRequest(input: unknown): PaymentRequest {
  const errors = validationErrors(input);
  if (errors.length > 0) {
    throw new Error(errors.join("; "));
  }

  const record = input as PaymentRequest;
  return {
    orderId: record.orderId,
    amountCents: record.amountCents,
    currency: record.currency,
    idempotencyKey: record.idempotencyKey,
  };
}
