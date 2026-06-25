# https://leetcode.com/problems/count-subarrays-with-majority-element-i/


class Solution:
    """3737. Count Subarrays With Majority Element I

    You are given an integer array `nums` and an integer `target`.

    Return the number of **subarrays** of `nums` in which `target` is the **majority
    element**.

    The **majority element** of a subarray is the element that appears **strictly**
    **more than half** of the times in that subarray.

    Constraints:

    * `1 <= nums.length <= 1000`

    * `1 <= nums[i] <= 10\u200b\u200b\u200b\u200b\u200b\u200b\u200b9`

    * `1 <= target <= 109`"""

    def count_majority_subarrays(self, nums: list[int], target: int) -> int: ...

    countMajoritySubarrays = count_majority_subarrays
