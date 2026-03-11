export interface HandlerShape {
  hasDatabase: boolean;
  hasExternalHttp: boolean;
  pureDecisionSteps: number;
}

export interface Repository<T extends { id: string }> {
  getById(id: string): T | undefined;
  list(): T[];
}

export function recommendedTestLayers(shape: HandlerShape): string[] {
  const layers: string[] = [];
  if (shape.pureDecisionSteps > 0) {
    layers.push("unit");
  }
  if (shape.hasDatabase) {
    layers.push("integration");
  }
  if (shape.hasExternalHttp) {
    layers.push("contract");
  }
  return layers;
}

export function fakeRepository<T extends { id: string }>(rows: T[]): Repository<T> {
  const data = new Map(rows.map((row) => [row.id, row]));
  return {
    getById(id: string) {
      return data.get(id);
    },
    list() {
      return [...data.values()];
    },
  };
}

export function handlerReadyForUnitTest(
  dependenciesInjected: boolean,
  hiddenGlobals: number,
): boolean {
  return dependenciesInjected && hiddenGlobals === 0;
}
