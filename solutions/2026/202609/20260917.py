# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/


class Solution:
    """1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

    You are given an array of integers `arr` and an integer `target`.

    You have to find **two non-overlapping sub-arrays** of `arr` each with a
    sum equal `target`. There can be multiple answers so you have to find an
    answer where the sum of the lengths of the two sub-arrays is **minimum**.

    Return *the minimum sum of the lengths* of the two required sub-arrays, or
    return `-1` if you cannot find such two sub-arrays.

    Constraints:

    * `1 <= arr.length <= 105`
    * `1 <= arr[i] <= 1000`
    * `1 <= target <= 108`
    """

    def min_sum_of_lengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        inf = n + 1
        # Shortest target subarray whose last index is <= current index.
        best_so_far = inf
        # best_ending_at_or_before[i] covers arr[: i + 1].
        prefix_best = [inf] * n
        left = 0
        window = 0
        answer = inf
        for right, value in enumerate(arr):
            window += value
            # Values are positive, so shrink until the window is <= target.
            while window > target:
                window -= arr[left]
                left += 1
            if window == target:
                length = right - left + 1
                # Pair this window with the best subarray fully to its left.
                prev = prefix_best[left - 1] if left else inf
                if prev < inf:
                    answer = min(answer, prev + length)
                best_so_far = min(best_so_far, length)
            prefix_best[right] = best_so_far
        return -1 if answer >= inf else answer

    minSumOfLengths = min_sum_of_lengths
