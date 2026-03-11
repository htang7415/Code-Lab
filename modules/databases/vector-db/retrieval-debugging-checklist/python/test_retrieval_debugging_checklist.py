import pytest

from retrieval_debugging_checklist import checklist_for_failure, checklist_report, first_step


def test_failure_modes_map_to_useful_first_steps():
    assert first_step("scope-leak") == "Verify workspace or tenant filters before similarity scoring"
    assert first_step("no-relevant-hit") == "Check whether relevant documents were chunked and indexed"
    assert first_step("ranked-below-k") == "Compare lexical, vector, and hybrid scores for the same query"


def test_report_expands_cases_into_query_specific_checklists():
    report = checklist_report(
        [
            {"query_id": "q1", "failure": "scope-leak"},
            {"query_id": "q2", "failure": "ranked-below-k"},
        ]
    )

    assert report["q1"][0].startswith("Verify workspace")
    assert report["q2"][0].startswith("Compare lexical")


def test_unknown_failure_raises():
    with pytest.raises(KeyError):
        checklist_for_failure("mystery")
