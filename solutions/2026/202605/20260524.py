# https://leetcode.com/problems/jump-game-v/


class Solution:
    """1340. Jump Game V

    Given an array of integers arr and an integer d. In one step you can jump from
    index i to index: i + x where i + x < arr.length and 0 < x <= d; or i - x
    where i - x >= 0 and 0 < x <= d. You can only jump from i to j if arr[i] >
    arr[j] and arr[i] > arr[k] for all k with min(i, j) < k < max(i, j). Start
    from any index and return the maximum number of indices you can visit. You
    cannot jump outside the array at any time.
    """

    def max_jumps(self, arr: list[int], d: int) -> int:
        n = len(arr)
        # dp[i] will hold the max number of indices visitable starting from i
        dp = [1] * n
        # Sort indices by increasing arr value to process lower heights first
        # This ensures when computing dp[i], all possible jump targets j have
        # already been processed
        indices = sorted(range(n), key=lambda x: arr[x])
        for i in indices:
            # Check possible right jumps
            for j in range(i + 1, min(i + d + 1, n)):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
            # Check possible left jumps
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] >= arr[i]:
                    break
                dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)

    maxJumps = max_jumps
