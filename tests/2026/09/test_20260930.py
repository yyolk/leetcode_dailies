def test_max_depth_after_split_examples(solution):
    # Example 1
    assert solution.maxDepthAfterSplit("(()())") == [0, 1, 1, 1, 1, 0]

    # Example 2 (official output is one valid split; this impl returns another)
    assert solution.maxDepthAfterSplit("()(())()") == [0, 0, 0, 1, 1, 0, 0, 0]


def test_max_depth_after_split_single_pair(solution):
    # Trivial VPS: one pair has depth 1, so either group is fine.
    assert solution.maxDepthAfterSplit("()") == [0, 0]
