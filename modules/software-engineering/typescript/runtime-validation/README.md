# Runtime Validation

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript types disappear at runtime, so untrusted data still needs explicit validation before it crosses into trusted application code.

## Key Points

- Compile-time safety does not validate JSON from a request, queue, or database.
- Runtime validation should report concrete errors instead of failing later in business logic.
- Parse at the boundary, then use the validated type internally.

## Minimal Code Mental Model

```typescript
const errors = validationErrors(input);
const valid = isPaymentRequest(input);
const request = parsePaymentRequest(input);
```

## Function

```typescript
export function validationErrors(input: unknown): string[];
export function isPaymentRequest(input: unknown): input is PaymentRequest;
export function parsePaymentRequest(input: unknown): PaymentRequest;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/runtime-validation/typescript/test_runtime_validation.ts
```
