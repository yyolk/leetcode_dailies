# https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/


class Solution:
    """3254. Find the Power of K-Size Subarrays I

    You are given an array of integers `nums` of length `n` and a *positive* integer
    `k`.

    The **power** of an array is defined as:

    * Its **maximum** element if *all* of its elements are **consecutive** and
    **sorted** in **ascending** order.

    * \\-1 otherwise.

    You need to find the **power** of all subarrays of `nums` of size `k`.

    Return an integer array `results` of size `n - k + 1`, where `results[i]` is the
    *power* of `nums[i..(i + k - 1)]`.

    """

    def results_array(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)

        # Special case for k=1, every single element is a valid subarray
        if k == 1:
            return nums

        results = []

        # Initialize variables for tracking consecutive elements
        i, consecutive_size = 1, 1

        # Loop through the array starting from the second element
        while i < n:
            # Check if current number is one more than the previous number
            if nums[i] - 1 == nums[i - 1]:
                consecutive_size += 1
            else:
                # Reset if not consecutive
                consecutive_size = 1

            # We start checking for subarrays once we have k-1 elements
            if i >= k - 1:
                # If we have at least k consecutive numbers, the power is the last number in this sequence
                if consecutive_size >= k:
                    # Note: The power isn't just the max; it's defined as the last element in the sequence
                    results.append(nums[i])
                else:
                    # Subarray does not meet power criteria
                    results.append(-1)

            i += 1

        return results

    resultsArray = results_array
