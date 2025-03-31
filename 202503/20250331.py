# https://leetcode.com/problems/put-marbles-in-bags/


class Solution:
    """2551. Put Marbles in Bags

    You have `k` bags. You are given a **0-indexed** integer array `weights` where
    `weights[i]` is the weight of the `ith` marble. You are also given the integer `k.`

    Divide the marbles into the `k` bags according to the following rules:

    * No bag is empty.

    * If the `ith` marble and `jth` marble are in a bag, then all marbles with an index
    between the `ith` and `jth` indices should also be in that same bag.

    * If a bag consists of all the marbles with an index from `i` to `j` inclusively,
    then the cost of the bag is `weights[i] + weights[j]`.

    The **score** after distributing the marbles is the sum of the costs of all the `k`
    bags.

    Return *the **difference** between the **maximum** and **minimum** scores among
    marble distributions*."""

    def put_marbles(self, weights: list[int], k: int) -> int:
        """
        Calculate the difference between maximum and minimum scores when distributing
        marbles into k bags.

        Args:
            weights (list[int]): Array of marble weights.
            k (int): Number of bags to distribute marbles into.

        Returns:
            int: Difference between maximum and minimum possible scores.
        """
        n = len(weights)
        
        # If k is 1 (one bag) or k equals n (each marble in its own bag),
        # there's only one possible score, so the difference is 0.
        if k == 1 or k == n:
            return 0
        
        # Compute the array of adjacent pair sums, representing the additional cost
        # added to the score when a split occurs between indices i and i+1.
        # For each split point p, we add weights[p] (end of one bag) and 
        # weights[p+1] (start of the next bag).
        A = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the array to efficiently access the smallest and largest pair sums.
        A.sort()
        
        # The minimum score includes weights[0] + weights[n-1] plus the sum of the
        # k-1 smallest pair sums. The maximum score includes weights[0] + weights[n-1]
        # plus the sum of the k-1 largest pair sums. The difference between max and min
        # scores is thus the difference between these two sums, as weights[0] and
        # weights[n-1] cancel out.
        max_sum = sum(A[-(k - 1):])  # Sum of the k-1 largest pair sums
        min_sum = sum(A[:k - 1])     # Sum of the k-1 smallest pair sums
        
        return max_sum - min_sum

    putMarbles = put_marbles
