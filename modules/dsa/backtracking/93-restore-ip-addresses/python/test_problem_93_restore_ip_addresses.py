from problem_93_restore_ip_addresses import Solution


def test_restore_ip_addresses_basic():
    result = Solution().restoreIpAddresses("25525511135")
    assert sorted(result) == ["255.255.11.135", "255.255.111.35"]


def test_restore_ip_addresses_short():
    assert Solution().restoreIpAddresses("1111") == ["1.1.1.1"]
