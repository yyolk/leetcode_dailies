# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/
MOD = 10**9 + 7


class Solution:
    """1420. Build Array Where You Can Find The Maximum Exactly K Comparisons

    You are given three integers `n`, `m` and `k`. Consider the following algorithm to find
    the maximum element of an array of positive integers:

        maximum_value = -1
        maximum_index = -1
        search_cost = 0
        n = arr.length
        for (i = 0; i < n; i++) {
            if (maximum_value < arr[i]) {
                maximum_value = arr[i]
                maximum_index = i
                search_cost = search_cost + 1
            }
        }
        return maximum_index

    You should build the array arr which has the following properties:

    * `arr` has exactly `n` integers.

    * `1 <= arr[i] <= m` where `(0 <= i < n)`.

    * After applying the mentioned algorithm to `arr`, the value `search_cost` is equal to
    `k`.

    Return *the number of ways* to build the array `arr` under the mentioned conditions. As
    the answer may grow large, the answer **must be** computed modulo `109 + 7`.
    """

    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """The different number of ways to build the array.

        Proposed solution using dynamic programming.

        Args:
            n (int): Length of arr.
            m (int): Maximum index of arr.
            k (int): The value of search_cost.

        Returns:
            int: The number of ways to build the array, arr, under the conditions.
        """
        # Initialize dynamic programming arrays
        dp = [[0] * (k + 1) for _ in range(m + 1)]
        prefix = [[0] * (k + 1) for _ in range(m + 1)]
        prev_dp = [[0] * (k + 1) for _ in range(m + 1)]
        prev_prefix = [[0] * (k + 1) for _ in range(m + 1)]

        # Initialize the base cases for cost = 1
        for j in range(1, m + 1):
            prev_dp[j][1] = 1
            prev_prefix[j][1] = j

        # Iterate through the lengths of the array (from 2 to n)
        for _ in range(2, n + 1):
            # Create new dp and prefix arrays for the current length
            dp = [[0] * (k + 1) for _ in range(m + 1)]
            prefix = [[0] * (k + 1) for _ in range(m + 1)]

            # Iterate through possible maximum numbers
            for max_num in range(1, m + 1):
                # Iterate through search costs
                for cost in range(1, k + 1):
                    # Calculate dp value for the current maxNum and cost
                    dp[max_num][cost] = (max_num * prev_dp[max_num][cost]) % MOD

                    # If maxNum > 1 and cost > 1, add previous prefix value
                    if max_num > 1 and cost > 1:
                        dp[max_num][cost] += prev_prefix[max_num - 1][cost - 1]
                        dp[max_num][cost] %= MOD

                    # Calculate the prefix sum for the current maxNum and cost
                    prefix[max_num][cost] = (
                        prefix[max_num - 1][cost] + dp[max_num][cost]
                    ) % MOD

            # Update the previous dp and prefix arrays for the next iteration
            prev_dp, prev_prefix = [row[:] for row in dp], [row[:] for row in prefix]

        # The result is stored in prefix[m][k]
        return prefix[m][k]
