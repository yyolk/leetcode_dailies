# https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/


class Solution:
    """3318. Find X-Sum of All K-Long Subarrays I

    You are given an array nums of n integers and two integers k and x.

    The x-sum of an array is calculated by the following procedure:

    Count the occurrences of all elements in the array.
    Keep only the occurrences of the top x most frequent elements. If two elements
    have the same number of occurrences, the element with the bigger value is
    considered more frequent.

    Calculate the sum of the resulting array.
    Note that if an array has less than x distinct elements, its x-sum is the sum of
    the array.

    Return an integer array answer of length n - k + 1 where answer[i] is the x-sum
    of the subarray nums[i..i + k - 1].
    """
    def find_x_sum(self, nums: list[int], k: int, x: int) -> list[int]:
        # Initialize result list
        res = []
        # Iterate over each possible starting index for subarrays of length k
        for i in range(len(nums) - k + 1):
            # Extract the current subarray
            sub = nums[i:i + k]
            # Count frequency of each element in the subarray
            from collections import Counter
            cnt = Counter(sub)
            # Get list of (value, frequency) pairs
            items = list(cnt.items())
            # Sort by descending frequency, then descending value
            items.sort(key=lambda p: (-p[1], -p[0]))
            # Select top x elements (or all if fewer than x)
            top = items[:x]
            # Calculate sum: value * frequency for each top element
            s = sum(val * freq for val, freq in top)
            # Append to result
            res.append(s)
        return res
    
    findXSum = find_x_sum