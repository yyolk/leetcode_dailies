from itertools import product


def brute_largest_integer(nums: list[int], k: int) -> int:
    counts: dict[int, int] = {}
    for start in range(len(nums) - k + 1):
        for value in set(nums[start : start + k]):
            counts[value] = counts.get(value, 0) + 1

    best = -1
    for value, count in counts.items():
        if count == 1:
            best = max(best, value)
    return best


def test_largest_integer_examples(solution):
    assert solution.largestInteger([3, 9, 2, 1, 7], 3) == 7
    assert solution.largestInteger([3, 9, 7, 2, 1, 7], 4) == 3
    assert solution.largestInteger([0, 0], 1) == -1


def test_largest_integer_matches_bruteforce(solution):
    for n in range(1, 8):
        for nums_tuple in product((0, 1, 2, 3), repeat=n):
            nums = list(nums_tuple)
            for k in range(1, n + 1):
                expected = brute_largest_integer(nums, k)
                actual = solution.largestInteger(nums, k)
                assert actual == expected, (nums, k, expected, actual)
