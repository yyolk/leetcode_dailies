# https://leetcode.com/problems/combination-sum-iv/


class Solution:
    """377. Combination Sum IV

    Given an array of **distinct** integers `nums` and a target integer `target`, return
    *the number of possible combinations that add up to* `target`.

    The test cases are generated so that the answer can fit in a **32-bit** integer.
    """

    def combinationSum4(self, nums: List[int], target: int) -> int:
        """How many combinations of nums add up to target

        Proposed solution, using dynamic programming. Does an exhaustive search.

        Args:
            nums (List of int): the input numbers to be used to find the combinations that
                add up to target
            target (int): the input target to find

        Returns:
            int: the number of possible combinations of input nums that add up to target
        """
        # Allocate our dp list, to our target + 1, to include the final number's sum
        # Each index will have how many combinations add to it's sum if index was a target
        dp = [0] * (target + 1)
        # There is one way to reach target sum of 0, by not choosing any number
        dp[0] = 1

        # Loop through all numbers from 1 to target (inclusive)
        for i in range(1, target + 1):
            # Loop through input nums for each value
            for num in nums:
                # Add the number of combinations to reach
                # i - num to the current dp[i] value if i >= num
                if i >= num:
                    dp[i] += dp[i - num]

        # After filling dp[], dp[target] is the number of combinations that sum to target
        return dp[target]
