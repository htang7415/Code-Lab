# Frontend-Backend Shared Types

> Track: `software-engineering` | Topic: `typescript`

## Concept

Shared TypeScript types can reduce drift across frontend and backend code, but only when the boundary is versioned clearly and runtime validation still protects network inputs.

## Key Points

- Shared packages do not eliminate API versioning.
- UI-facing projections should stay narrower than server storage records.
- Shared types help most when multiple clients consume the same stable contract.

## Minimal Code Mental Model

```typescript
const card = toUserCard({
  id: "u_1",
  displayName: "Alex",
  role: "admin",
  version: 2,
});
const compatible = schemaVersionsCompatible(2, 2);
```

## Function

```typescript
export function toUserCard(user: ApiUser): UserCard;
export function schemaVersionsCompatible(clientVersion: number, serverVersion: number): boolean;
export function shouldShareType(sharedConsumers: number, breakingChangesLastQuarter: number): boolean;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/frontend-backend-shared-types/typescript/test_frontend_backend_shared_types.ts
```
