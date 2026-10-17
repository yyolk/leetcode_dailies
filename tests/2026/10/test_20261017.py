def test_min_swaps_examples(solution):
    # Official Example 1: nums = [37, 100] -> 1
    assert solution.minSwaps([37, 100]) == 1

    # Official Example 2: nums = [22, 14, 33, 7] -> 0
    assert solution.minSwaps([22, 14, 33, 7]) == 0

    # Official Example 3: nums = [18, 43, 34, 16] -> 2
    assert solution.minSwaps([18, 43, 34, 16]) == 2


def test_min_swaps_single(solution):
    # Single element is already sorted: 0 swaps.
    assert solution.minSwaps([42]) == 0
