def test_sort_permutation_examples(solution):
    # Official Example 1: nums = [0,3,2,1] -> 1
    assert solution.sortPermutation([0, 3, 2, 1]) == 1

    # Official Example 2: nums = [0,1,3,2] -> 2
    assert solution.sortPermutation([0, 1, 3, 2]) == 2

    # Official Example 3: nums = [3,2,1,0] -> 0
    assert solution.sortPermutation([3, 2, 1, 0]) == 0


def test_sort_permutation_single(solution):
    # Single element is already sorted; expected output is 0 by the spec.
    assert solution.sortPermutation([0]) == 0
