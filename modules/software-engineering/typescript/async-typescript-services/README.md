# Async TypeScript Services

> Track: `software-engineering` | Topic: `typescript`

## Concept

Typed async services should make backpressure, deadlines, and failure shape explicit instead of returning unstructured promises that force every caller to guess.

## Key Points

- Async code still needs typed success and failure paths.
- Backpressure should be decided before starting more work.
- Deadline math should stay explicit because timeout bugs are usually operational bugs.

## Minimal Code Mental Model

```typescript
const budget = concurrencyBudget(4, 8);
const result = await callWithBudget(3, budget, async () => "ok");
const retry = shouldRetry(result);
```

## Function

```typescript
export function concurrencyBudget(workers: number, perWorkerLimit: number): number;
export function deadlineRemaining(timeoutMs: number, elapsedMs: number): number;
export function shouldRetry<T>(result: ServiceResult<T>): boolean;
export async function callWithBudget<T>(
  inFlight: number,
  limit: number,
  task: () => Promise<T>,
): Promise<ServiceResult<T>>;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/async-typescript-services/typescript/test_async_typescript_services.ts
```
