# Type-Driven API Design

> Track: `software-engineering` | Topic: `typescript`

## Concept

TypeScript is most useful at API boundaries when the request and response shapes make invalid states harder to represent in the first place.

## Key Points

- The stable contract should be expressed as named types, not scattered object literals.
- Patch types should expose only fields that are actually mutable.
- Type guards help keep the runtime and the compile-time model aligned.

## Minimal Code Mental Model

```typescript
const updated = applyUserPatch(user, { displayName: "A. Lee", active: false });
const fields = updatableFields({ role: "editor", active: true });
const complete = isCompleteUserRecord(updated);
```

## Function

```typescript
export function applyUserPatch(user: UserRecord, patch: UserPatch): UserRecord;
export function updatableFields(patch: UserPatch): Array<keyof UserPatch>;
export function isCompleteUserRecord(value: Partial<UserRecord>): value is UserRecord;
```

## Run tests

```bash
pnpm --dir web exec tsx --test ../modules/software-engineering/typescript/type-driven-api-design/typescript/test_type_driven_api_design.ts
```
