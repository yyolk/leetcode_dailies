# https://leetcode.com/problems/house-robber-iv/


class Solution:
    """2560. House Robber IV

    There are several consecutive houses along a street, each of which has some money
    inside. There is also a robber, who wants to steal money from the homes, but he
    **refuses to steal from adjacent homes**.

    The **capability** of the robber is the maximum amount of money he steals from one
    house of all the houses he robbed.

    You are given an integer array `nums` representing how much money is stashed in each
    house. More formally, the `ith` house from the left has `nums[i]` dollars.

    You are also given an integer `k`, representing the **minimum** number of houses the
    robber will steal from. It is always possible to steal at least `k` houses.

    Return *the **minimum** capability of the robber out of all the possible ways to
    steal at least* `k` *houses*."""

    def min_capability(self, nums: list[int], k: int) -> int:
        def can_select_at_least_k(m: int) -> bool:
            """
            Checks if it's possible to select at least k non-adjacent houses with money <= m.

            Args:
                m (int): Candidate capability value.

            Returns:
                bool: True if at least k houses can be selected, False otherwise.
            """
            count = 0
            prev_selected = False
            for num in nums:
                if num <= m and not prev_selected:
                    count += 1
                    prev_selected = True
                else:
                    prev_selected = False
            return count >= k

        # Binary search on the capability value
        left, right = 1, 10**9
        while left < right:
            mid = (left + right) // 2
            if can_select_at_least_k(mid):
                # If possible with mid, try a smaller capability
                right = mid
            else:
                # If not possible, increase the capability
                left = mid + 1
        return left

    minCapability = min_capability
