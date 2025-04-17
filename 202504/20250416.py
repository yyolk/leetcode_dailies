# https://leetcode.com/problems/count-the-number-of-good-subarrays/


class Solution:
    """2537. Count the Number of Good Subarrays

    Given an integer array `nums` and an integer `k`, return *the number of **good**
    subarrays of* `nums`.

    A subarray `arr` is **good** if there are **at least** `k` pairs of indices `(i, j)`
    such that `i < j` and `arr[i] == arr[j]`.

    A **subarray** is a contiguous **non-empty** sequence of elements within an array.
    """

    def count_good(self, nums: list[int], k: int) -> int:
        n = len(nums)
        # Initialize sliding window variables
        left = 0
        current_pairs = 0
        freq = defaultdict(int)  # Frequency of elements in the current window
        count_less_than_k = 0  # Number of subarrays with < k pairs

        # Iterate over all possible right endpoints
        for right in range(n):
            x = nums[right]
            # Adding nums[right] increases pairs by current frequency of x
            current_pairs += freq[x]
            freq[x] += 1

            # Shrink window until current_pairs < k
            while current_pairs >= k and left <= right:
                y = nums[left]
                freq[y] -= 1
                # Removing nums[left] decreases pairs by remaining frequency
                current_pairs -= freq[y]
                if freq[y] == 0:
                    del freq[y]  # Clean up dictionary
                left += 1

            # All subarrays [l, right] with l >= left have < k pairs
            count_less_than_k += right - left + 1

        # Total subarrays = n * (n + 1) / 2
        total_subarrays = n * (n + 1) // 2
        # Good subarrays = total - subarrays with < k pairs
        return total_subarrays - count_less_than_k

    countGood = count_good
