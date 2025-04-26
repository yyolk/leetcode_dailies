# https://leetcode.com/problems/count-of-interesting-subarrays/


class Solution:
    """2845. Count of Interesting Subarrays

    You are given a **0-indexed** integer array `nums`, an integer `modulo`, and an
    integer `k`.

    Your task is to find the count of subarrays that are **interesting**.

    A **subarray** `nums[l..r]` is **interesting** if the following condition holds:

    * Let `cnt` be the number of indices `i` in the range `[l, r]` such that `nums[i] %
    modulo == k`. Then, `cnt % modulo == k`.

    Return *an integer denoting the count of interesting subarrays.*

    **Note:** A subarray is *a contiguous non-empty sequence of elements within an
    array*."""

    def count_interesting_subarrays(self, nums: list[int], modulo: int, k: int) -> int:
        # Initialize frequency map with 0 sum having frequency 1
        freq = {0: 1}
        current_sum = 0  # Running sum of indicator values
        total_count = 0  # Count of interesting subarrays

        # Iterate through each element in nums
        for num in nums:
            # Indicator is 1 if num % modulo == k, else 0
            indicator = 1 if num % modulo == k else 0
            current_sum += indicator  # Update prefix sum

            # Current prefix sum modulo modulo
            prefix_mod = current_sum % modulo

            # Target value that prefix_sum[l] % modulo should equal
            target = (prefix_mod - k) % modulo

            # If target exists in freq, add its frequency to total_count
            if target in freq:
                total_count += freq[target]

            # Update frequency of current prefix_mod
            if prefix_mod in freq:
                freq[prefix_mod] += 1
            else:
                freq[prefix_mod] = 1

        return total_count

    countInterestingSubarrays = count_interesting_subarrays
