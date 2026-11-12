def test_longest_monotonic_subarray_examples(solution):
    # Official Example 1.
    assert solution.longestMonotonicSubarray([1, 4, 3, 3, 2]) == 2

    # Official Example 2.
    assert solution.longestMonotonicSubarray([3, 3, 3, 3]) == 1

    # Official Example 3.
    assert solution.longestMonotonicSubarray([3, 2, 1]) == 3


def test_longest_monotonic_subarray_single(solution):
    # Trivial single-element case.
    assert solution.longestMonotonicSubarray([42]) == 1


def test_longest_monotonic_subarray_mixed(solution):
    # Increasing then decreasing: longest is the decreasing run of 4.
    # Manually verified: [1,3,2,0,-1] has decr streak 4 (3>2>0>-1).
    assert solution.longestMonotonicSubarray([1, 3, 2, 0, -1]) == 4
