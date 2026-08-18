def expected_missing_integer(nums: list[int]) -> int:
    prefix_sum = nums[0]
    i = 1
    while i < len(nums) and nums[i] == nums[i - 1] + 1:
        prefix_sum += nums[i]
        i += 1

    present = set(nums)
    while prefix_sum in present:
        prefix_sum += 1
    return prefix_sum

def test_smallest_missing_integer_examples(solution):
    assert solution.missingInteger([1, 2, 3, 2, 5]) == 6
    assert solution.missingInteger([3, 4, 5, 1, 12, 14, 13]) == 15

def test_smallest_missing_integer_prefix_and_gaps(solution):
    assert solution.missingInteger([10]) == 11
    assert solution.missingInteger([1, 2, 3, 4]) == 10
    assert solution.missingInteger([2, 3, 4, 9, 10, 11]) == 12
    assert solution.missingInteger([5, 1, 2, 3]) == 6

def test_smallest_missing_integer_matches_reference_cases(solution):
    cases = [
        [1, 2, 3, 4, 6, 7, 8],
        [4, 5, 6, 7, 1, 2, 3, 22],
        [8, 9, 10, 11, 12],
        [7, 3, 4, 5, 6],
        [1, 2, 2, 3, 4, 5],
        [2, 3, 4, 5, 14, 15],
        [9, 10, 11, 12, 13, 55, 56],
    ]
    for nums in cases:
        expected = expected_missing_integer(nums)
        actual = solution.missingInteger(nums)
        assert actual == expected, (nums, expected, actual)
