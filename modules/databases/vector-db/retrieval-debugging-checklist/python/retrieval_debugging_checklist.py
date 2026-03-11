"""retrieval_debugging_checklist - map failure modes to the next useful debugging steps."""

from __future__ import annotations


CHECKLISTS = {
    "scope-leak": [
        "Verify workspace or tenant filters before similarity scoring",
        "Check access-control metadata on indexed chunks",
        "Inspect top-k results for wrong-tenant documents",
    ],
    "no-relevant-hit": [
        "Check whether relevant documents were chunked and indexed",
        "Compare lexical and vector recall on the missed queries",
        "Inspect embedding model, preprocessing, and metadata coverage",
    ],
    "ranked-below-k": [
        "Compare lexical, vector, and hybrid scores for the same query",
        "Inspect hybrid weights, reranker inputs, and metadata filters",
        "Measure reciprocal rank before and after reranking",
    ],
    "ok": [
        "No action needed; keep this query as a regression check",
    ],
}


def checklist_for_failure(failure: str) -> list[str]:
    if failure not in CHECKLISTS:
        raise KeyError(failure)
    return list(CHECKLISTS[failure])


def first_step(failure: str) -> str:
    return checklist_for_failure(failure)[0]


def checklist_report(cases: list[dict[str, str]]) -> dict[str, list[str]]:
    return {
        case["query_id"]: checklist_for_failure(case["failure"])
        for case in cases
    }
