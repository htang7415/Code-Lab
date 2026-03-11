from join_elimination_basics import join_can_be_eliminated, plan_summary


def test_redundant_parent_join_can_be_eliminated_when_fk_guarantees_match():
    summary = plan_summary(
        child_rows=1_000,
        parent_lookup_cost=2,
        selects_parent_columns=False,
        filters_parent_rows=False,
        child_fk_not_null=True,
    )

    assert join_can_be_eliminated(False, False, True) is True
    assert summary["eliminated"] is True
    assert int(summary["work_after_elimination"]) < int(summary["work_with_join"])


def test_parent_columns_or_filters_block_elimination():
    assert join_can_be_eliminated(True, False, True) is False
    assert join_can_be_eliminated(False, True, True) is False
    assert join_can_be_eliminated(False, False, False) is False
