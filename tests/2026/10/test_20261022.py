def test_min_operations_examples(solution):
    # Official Example 1: nums = [0, 2, 1] -> 2
    assert solution.minOperations([0, 2, 1]) == 2

    # Official Example 2: nums = [1, 0, 2] -> 2
    assert solution.minOperations([1, 0, 2]) == 2

    # Official Example 3: nums = [2, 0, 1, 3] -> -1
    assert solution.minOperations([2, 0, 1, 3]) == -1


def test_min_operations_single(solution):
    # Single element is already sorted; expected output is 0 by the spec.
    assert solution.minOperations([0]) == 0
