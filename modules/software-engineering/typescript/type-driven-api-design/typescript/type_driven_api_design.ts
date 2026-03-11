export type UserRole = "admin" | "editor" | "viewer";

export interface UserRecord {
  id: string;
  email: string;
  displayName: string;
  role: UserRole;
  active: boolean;
}

export type UserPatch = Partial<Pick<UserRecord, "displayName" | "role" | "active">>;

const PATCHABLE_FIELDS = ["displayName", "role", "active"] as const;

export function applyUserPatch(user: UserRecord, patch: UserPatch): UserRecord {
  return { ...user, ...patch };
}

export function updatableFields(patch: UserPatch): Array<keyof UserPatch> {
  return PATCHABLE_FIELDS.filter((field) => field in patch);
}

export function isCompleteUserRecord(value: Partial<UserRecord>): value is UserRecord {
  return (
    typeof value.id === "string" &&
    value.id.length > 0 &&
    typeof value.email === "string" &&
    value.email.includes("@") &&
    typeof value.displayName === "string" &&
    value.displayName.length > 0 &&
    (value.role === "admin" || value.role === "editor" || value.role === "viewer") &&
    typeof value.active === "boolean"
  );
}
