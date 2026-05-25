# https://leetcode.com/problems/jump-game-vii/

class Solution:
    """1871. Jump Game VII

    You are given a 0-indexed binary string s and two integers min_jump and
    max_jump. In the beginning, you are standing at index 0, which is equal to
    '0'. You can move from index i to index j if the following conditions are
    fulfilled: i + min_jump <= j <= min(i + max_jump, s.length - 1), and
    s[j] == '0'. Return true if you can reach index s.length - 1 in s, or false
    otherwise.
    """
    def can_reach(self, s: str, min_jump: int, max_jump: int) -> bool:
        n = len(s)
        # dp marks reachable positions; start at 0 always true
        dp = [False] * n
        dp[0] = True
        # count of reachable predecessors in current sliding window
        count = 0
        for i in range(min_jump, n):
            # newly added predecessor at the right of window
            count += dp[i - min_jump]
            # remove predecessor that slid out of left of window
            if i - max_jump > 0:
                count -= dp[i - max_jump - 1]
            # set current reachable only if count > 0 and safe landing
            if count > 0 and s[i] == "0":
                dp[i] = True
        return dp[n - 1]

    canReach = can_reach