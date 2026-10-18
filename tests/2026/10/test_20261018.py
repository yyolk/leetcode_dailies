def test_num_of_ways_examples(solution):
    # Official Example 1: nums = [2,1,3] -> 1
    assert solution.numOfWays([2, 1, 3]) == 1

    # Official Example 2: nums = [3,4,5,1,2] -> 5
    assert solution.numOfWays([3, 4, 5, 1, 2]) == 5

    # Official Example 3: nums = [1,2,3] -> 0
    assert solution.numOfWays([1, 2, 3]) == 0


def test_num_of_ways_single(solution):
    # Single element: only one way, so 0 other ways.
    assert solution.numOfWays([1]) == 0
