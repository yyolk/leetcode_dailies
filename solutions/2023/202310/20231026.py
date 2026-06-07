# https://leetcode.com/problems/binary-trees-with-factors/
MOD = 10**9 + 7


class Solution:
    """823. Binary Trees With Factors

    Given an array of unique integers, `arr`, where each integer `arr[i]` is strictly
    greater than `1`.

    We make a binary tree using these integers, and each number may be used for any
    number of times. Each non-leaf node's value should be equal to the product of the
    values of its children.

    Return *the number of binary trees we can make*. The answer may be too large so
    return the answer **modulo** `109 + 7`.
    """

    def num_factored_binary_trees(self, arr: list[int]) -> int:
        """The number of binary trees that we can make from the input arr.

        Proposed solution using dynamic programming.

        Args:
            arr (list of int): Input array of unique integers, all are greater than 1.
        Returns:
            int: The number of binary trees we can make from the input.
        """
        arr.sort()
        # Create a set for faster lookup
        s = set(arr)
        # Instantiate a dynamic programming dictionar, where dp[x] stores the
        # number of binary trees that can be formed with root value x
        dp = {x: 1 for x in arr}

        # Iterate through the elements in the array
        for i in arr:
            # Iterate through the elements again
            for j in arr:
                # If j is greater than the square root of i, break the loop
                if j > i**0.5:
                    break
                # Check if j is a factor of i and the complement (i // j) is in the set
                if i % j == 0 and i // j in s:
                    # If j and the complement are the same, add dp[j] * dp[j] to dp[i]
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    # Otherwise, add dp[j] * dp[i // j] * 2 to dp[i]
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    # Apply the modulo operation to the result
                    dp[i] %= MOD

        # Sum up all the values in dp and apply the modulo operation to the final result
        return sum(dp.values()) % MOD

    numFactoredBinaryTrees = num_factored_binary_trees
