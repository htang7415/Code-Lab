export type ServiceResult<T> =
  | { ok: true; value: T }
  | { ok: false; retryable: boolean; reason: string };

export function concurrencyBudget(workers: number, perWorkerLimit: number): number {
  return Math.max(workers, 0) * Math.max(perWorkerLimit, 0);
}

export function deadlineRemaining(timeoutMs: number, elapsedMs: number): number {
  return Math.max(timeoutMs - elapsedMs, 0);
}

export function shouldRetry<T>(result: ServiceResult<T>): boolean {
  return result.ok === false && result.retryable;
}

export async function callWithBudget<T>(
  inFlight: number,
  limit: number,
  task: () => Promise<T>,
): Promise<ServiceResult<T>> {
  if (inFlight >= limit) {
    return { ok: false, retryable: true, reason: "backpressure" };
  }

  try {
    return { ok: true, value: await task() };
  } catch (error) {
    return {
      ok: false,
      retryable: false,
      reason: error instanceof Error ? error.message : "unknown-error",
    };
  }
}
