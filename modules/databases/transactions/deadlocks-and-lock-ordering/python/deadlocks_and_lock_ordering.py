"""deadlocks_and_lock_ordering - detect lock order inversions and canonicalize them."""

from __future__ import annotations


def inversion_pairs(order_a: list[str], order_b: list[str]) -> list[tuple[str, str]]:
    pos_a = {resource: index for index, resource in enumerate(order_a)}
    pos_b = {resource: index for index, resource in enumerate(order_b)}
    shared = [resource for resource in order_a if resource in pos_b]
    inversions: list[tuple[str, str]] = []

    for left_index, left in enumerate(shared):
        for right in shared[left_index + 1 :]:
            if pos_a[left] < pos_a[right] and pos_b[left] > pos_b[right]:
                inversions.append((left, right))

    return inversions


def has_deadlock_risk(order_a: list[str], order_b: list[str]) -> bool:
    return len(inversion_pairs(order_a, order_b)) > 0


def canonical_lock_order(resources: list[str]) -> list[str]:
    return sorted(dict.fromkeys(resources))


def apply_canonical_order(
    transaction_requests: dict[str, list[str]],
) -> dict[str, list[str]]:
    return {
        txn_id: canonical_lock_order(resources)
        for txn_id, resources in transaction_requests.items()
    }
