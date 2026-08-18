from itertools import product
def brute_max_subarray_length(nums: list[int], k: int) -> int:
    best = 0
    for left in range(len(nums)):
        counts: dict[int, int] = {}
        for right in range(left, len(nums)):
            value = nums[right]
            counts[value] = counts.get(value, 0) + 1
            if counts[value] > k:
                break
            best = max(best, right - left + 1)
    return best

def test_length_of_longest_subarray_with_at_most_k_frequency_examples(solution):
    assert solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2) == 6
    assert solution.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1) == 2
    assert solution.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4) == 4

def test_length_of_longest_subarray_with_at_most_k_frequency_matches_bruteforce(solution):
    for n in range(1, 8):
        for nums_tuple in product((1, 2, 3), repeat=n):
            nums = list(nums_tuple)
            for k in range(1, n + 1):
                expected = brute_max_subarray_length(nums, k)
                actual = solution.maxSubarrayLength(nums, k)
                assert actual == expected, (nums, k, expected, actual)
