def test_can_alice_win_examples(solution):
    # Official Example 1.
    assert solution.canAliceWin(12) is True

    # Official Example 2.
    assert solution.canAliceWin(1) is False


def test_can_alice_win_exact_ten(solution):
    # Alice removes exactly 10 stones and wins immediately.
    assert solution.canAliceWin(10) is True
