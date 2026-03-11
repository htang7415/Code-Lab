# Testing TypeScript Backends

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript backend handlers become easier to test when request parsing, pure decisions, and side effects are separated behind small typed seams.

## Key Points

- A handler with hidden globals is harder to unit test no matter how good the types are.
- Fake repositories are useful when the contract is small and deterministic.
- Contract tests matter once the handler crosses a network-owned boundary.

## Minimal Code Mental Model

```typescript
const layers = recommendedTestLayers({
  hasDatabase: true,
  hasExternalHttp: true,
  pureDecisionSteps: 2,
});
const ready = handlerReadyForUnitTest(true, 0);
```

## Function

```typescript
export function recommendedTestLayers(shape: HandlerShape): string[];
export function fakeRepository<T extends { id: string }>(rows: T[]): Repository<T>;
export function handlerReadyForUnitTest(dependenciesInjected: boolean, hiddenGlobals: number): boolean;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/testing-typescript-backends/typescript/test_testing_typescript_backends.ts
```
