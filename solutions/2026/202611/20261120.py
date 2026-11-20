# https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

from collections import defaultdict


class Solution:
    """3041. Maximize Consecutive Elements in an Array After Modification

    You are given a 0-indexed array nums consisting of positive integers.

    Initially, you can increase the value of any element in the array by at most 1.

    After that, you need to select one or more elements from the final array such
    that those elements are consecutive when sorted in increasing order. For
    example, the elements [3, 4, 5] are consecutive while [3, 4, 6] and [1, 1, 2,
    3] are not.

    Return the maximum number of elements that you can select.

    Constraints:

    * 1 <= nums.length <= 10**5

    * 1 <= nums[i] <= 10**6
    """

    def max_selected_elements(self, nums: list[int]) -> int:
        # Sort so we process values in increasing order.
        nums.sort()
        # dp[x] holds the longest consecutive sequence ending at value x.
        dp = defaultdict(int)
        ans = 0
        for num in nums:
            # Prefer the choice that uses this element as num+1 (extends from num).
            # Then update the choice that uses it as num (extends from num-1).
            # Processing order ensures multiples are handled without reuse.
            dp[num + 1] = dp[num] + 1
            dp[num] = dp[num - 1] + 1
            ans = max(ans, dp[num], dp[num + 1])
        return ans

    maxSelectedElements = max_selected_elements
