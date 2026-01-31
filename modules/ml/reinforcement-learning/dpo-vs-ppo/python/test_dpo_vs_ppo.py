from dpo_vs_ppo import compare_methods


def test_compare_methods():
    assert "dpo" in compare_methods()
