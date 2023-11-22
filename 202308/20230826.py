# https://leetcode.com/problems/maximum-length-of-pair-chain/


class Solution:
    """646. Maximum Length of Pair Chain

    You are given an array of n pairs pairs where
    pairs[i] = [lefti, righti] and lefti < righti.

    A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c.
    A chain of pairs can be formed in this fashion.

    Return the length longest chain which can be formed.

    You do not need to use up all the given intervals.
    You can select pairs in any order.
    """

    def findLongestChain(self, pairs: list[list[int]]) -> int:
        """A chain of pairs in sequnetial order from a pairs list

        A pair group where pairs[i] = [left_i, right_i] and left_i < right_i

        Pairs can be selected in any order. You do not need to use all pairs

        The proposed solution uses dynamic programming.

        Args:
            pairs (list of list of int): A list of pairs that are the input

        Returns:
            int: length of the longest chain that can be produced
        """
        # Sort the whole thing by the second item in each group
        pairs.sort(key=lambda x: x[1])

        n = len(pairs)
        dp = [1] * n  # initialize a dp array with 1 as the minimum length

        for i in range(1, n):
            for j in range(i):
                # compare this with the previous
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
