def test_minimum_deletions_examples(solution):
    assert solution.minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]) == 5
    assert solution.minimumDeletions([0, -4, 19, 1, 8, -2, -3, 5]) == 3
    assert solution.minimumDeletions([101]) == 1
