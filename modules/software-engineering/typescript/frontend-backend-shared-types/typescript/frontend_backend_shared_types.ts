export interface ApiUser {
  id: string;
  displayName: string;
  role: "admin" | "member";
  version: number;
}

export interface UserCard {
  id: string;
  label: string;
  canManage: boolean;
}

export function toUserCard(user: ApiUser): UserCard {
  return {
    id: user.id,
    label: user.displayName,
    canManage: user.role === "admin",
  };
}

export function schemaVersionsCompatible(
  clientVersion: number,
  serverVersion: number,
): boolean {
  return clientVersion === serverVersion;
}

export function shouldShareType(
  sharedConsumers: number,
  breakingChangesLastQuarter: number,
): boolean {
  return sharedConsumers >= 2 && breakingChangesLastQuarter <= 1;
}
