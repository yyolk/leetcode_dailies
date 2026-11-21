def test_find_subtree_sizes_examples(solution):
    # Official Example 1.
    assert solution.findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc") == [
        6,
        3,
        1,
        1,
        1,
        1,
    ]

    # Official Example 2.
    assert solution.findSubtreeSizes([-1, 0, 4, 0, 1], "abbba") == [5, 2, 1, 1, 1]

    # Trivial single-element case (obvious from spec).
    assert solution.findSubtreeSizes([-1], "a") == [1]
