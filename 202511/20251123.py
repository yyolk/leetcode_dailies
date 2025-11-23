# https://leetcode.com/problems/greatest-sum-divisible-by-three/


class Solution:
    """1262. Greatest Sum Divisible by Three

    Given an integer array nums, return the maximum possible sum of elements
    of the array such that the sum is divisible by three.

    Approach: DP where dp[i] = maximum sum achievable with remainder i.
    We only need to track remainders 0, 1, 2.
    """
    def max_sum_div_three(self, nums: list[int]) -> int:
        # dp[0]: max sum ≡ 0 (mod 3), dp[1]: ≡ 1, dp[2]: ≡ 2
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            r = num % 3                     # current number's remainder
            # create a copy because we update using previous values
            prev = dp[:]
            
            for rem in range(3):
                if prev[rem] != float('-inf'):        # valid previous state
                    new_rem = (rem + r) % 3           # new remainder after adding num
                    dp[new_rem] = max(dp[new_rem], prev[rem] + num)
        
        return int(dp[0])   # dp[0] is always non-negative after processing
        

    maxSumDivThree = max_sum_div_three