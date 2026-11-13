# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

from collections import deque


class Solution:
    """3420. Count Non-Decreasing Subarrays After K Operations

    You are given an array `nums` of `n` integers and an integer `k`.

    For each subarray of `nums`, you can apply **up to** `k` operations
    on it. In each operation, you increment any element of the subarray
    by 1.

    **Note** that each subarray is considered independently, meaning
    changes made to one subarray do not persist to another.

    Return the number of subarrays that you can make **non-decreasing**
    after performing at most `k` operations.

    An array is said to be **non-decreasing** if each element is greater
    than or equal to its previous element, if it exists.

    Constraints:

    * `1 <= nums.length <= 105`

    * `1 <= nums[i] <= 109`

    * `1 <= k <= 109`"""

    def count_non_decreasing_subarrays(self, nums: list[int], k: int) -> int:
        # Sliding window from right to left. Deque holds indices of candidate
        # prefix maxima in decreasing order of value. cnt tracks the total
        # cost (increments) to make the current window non-decreasing.
        result = 0
        cnt = 0
        dq = deque()
        right = len(nums) - 1
        for left in range(len(nums) - 1, -1, -1):
            # Merge segments that the new left element dominates.
            while dq and nums[dq[-1]] < nums[left]:
                l = dq.pop()
                r = dq[-1] - 1 if dq else right
                cnt += (r - l + 1) * (nums[left] - nums[l])
            dq.append(left)
            # Shrink the right end until the cost is at most k.
            while cnt > k:
                cnt -= nums[dq[0]] - nums[right]
                if dq[0] == right:
                    dq.popleft()
                right -= 1
            # All subarrays [left, left], ..., [left, right] are valid.
            result += right - left + 1
        return result

    countNonDecreasingSubarrays = count_non_decreasing_subarrays
