# https://leetcode.com/problems/count-the-number-of-fair-pairs/


class Solution:
    """2563. Count the Number of Fair Pairs

    Given a **0-indexed** integer array `nums` of size `n` and two integers `lower` and
    `upper`, return *the number of fair pairs*.

    A pair `(i, j)` is **fair** if:

    * `0 <= i < j < n`, and

    * `lower <= nums[i] + nums[j] <= upper`"""

    def count_fair_pairs(self, nums: list[int], lower: int, upper: int) -> int:
        # Helper function to count pairs with sum <= target
        def count_pairs_less_equal(target: int) -> int:
            left = 0
            right = len(nums) - 1
            count = 0
            while left < right:
                if nums[left] + nums[right] <= target:
                    # All indices from left+1 to right form valid pairs with left
                    count += right - left
                    left += 1
                else:
                    right -= 1
            return count

        # Sort the array to enable two-pointer technique
        nums.sort()

        # Count pairs with sum <= upper
        pairs_up_to_upper = count_pairs_less_equal(upper)

        # Count pairs with sum < lower by using lower - 1
        # Since sums are integers, sum < lower is equivalent to sum <= lower - 1
        pairs_below_lower = count_pairs_less_equal(lower - 1)

        # Number of pairs with lower <= sum <= upper
        return pairs_up_to_upper - pairs_below_lower

    countFairPairs = count_fair_pairs
