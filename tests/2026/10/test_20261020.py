def test_sortable_integers_examples(solution):
    # Official Example 1: nums = [3,1,2] -> 3
    assert solution.sortableIntegers([3, 1, 2]) == 3

    # Official Example 2: nums = [7,6,5] -> 0
    assert solution.sortableIntegers([7, 6, 5]) == 0

    # Official Example 3: nums = [5,8] -> 3
    assert solution.sortableIntegers([5, 8]) == 3


def test_sortable_integers_single(solution):
    # Single element: only k=1 is sortable, sum is 1.
    assert solution.sortableIntegers([42]) == 1
