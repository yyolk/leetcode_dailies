def test_target_indices_examples(solution):
    # Official Example 1: nums = [1,2,5,2,3], target = 2 -> [1,2]
    assert solution.targetIndices([1, 2, 5, 2, 3], 2) == [1, 2]

    # Official Example 2: nums = [1,2,5,2,3], target = 3 -> [3]
    assert solution.targetIndices([1, 2, 5, 2, 3], 3) == [3]

    # Official Example 3: nums = [1,2,5,2,3], target = 5 -> [4]
    assert solution.targetIndices([1, 2, 5, 2, 3], 5) == [4]


def test_target_indices_empty(solution):
    # Target not present: empty list (obvious from spec).
    assert solution.targetIndices([1, 2, 5, 2, 3], 4) == []


def test_target_indices_single(solution):
    # Single element matching target: index 0.
    assert solution.targetIndices([7], 7) == [0]
