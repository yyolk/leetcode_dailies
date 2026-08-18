from itertools import product


def brute_longest_subsequence(nums: list[int]) -> int:
    n = len(nums)
    best = 0
    for mask in range(1, 1 << n):
        xor_value = 0
        length = 0
        for i in range(n):
            if (mask >> i) & 1:
                xor_value ^= nums[i]
                length += 1
        if xor_value != 0:
            best = max(best, length)
    return best


def test_longest_subsequence_with_non_zero_bitwise_xor_examples(solution):
    assert solution.longestSubsequence([1, 2, 3]) == 2
    assert solution.longestSubsequence([3, 5, 2]) == 3
    assert solution.longestSubsequence([0, 0]) == 0


def test_longest_subsequence_with_non_zero_bitwise_xor_matches_bruteforce(solution):
    for n in range(1, 8):
        for nums_tuple in product((0, 1, 2, 3), repeat=n):
            nums = list(nums_tuple)
            expected = brute_longest_subsequence(nums)
            actual = solution.longestSubsequence(nums)
            assert actual == expected, (nums, expected, actual)
