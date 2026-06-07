# https://leetcode.com/problems/range-product-queries-of-powers/
# Define the modulo constant as 10^9 + 7 to prevent integer overflow
MOD = 10**9 + 7


class Solution:
    """2438. Range Product Queries of Powers

    Given a positive integer `n`, there exists a **0-indexed** array called `powers`,
    composed of the **minimum** number of powers of `2` that sum to `n`. The array is
    sorted in **non-decreasing** order, and there is **only one** way to form the array.

    You are also given a **0-indexed** 2D integer array `queries`, where `queries[i] =
    [lefti, righti]`. Each `queries[i]` represents a query where you have to find the
    product of all `powers[j]` with `lefti <= j <= righti`.

    Return *an array* `answers`*, equal in length to* `queries`*, where* `answers[i]`
    *is the answer to the* `ith` *query*. Since the answer to the `ith` query may be too
    large, each `answers[i]` should be returned **modulo** `109 + 7`."""

    def product_queries(self, n: int, queries: list[list[int]]) -> list[int]:
        # Initialize an empty list to store the exponents where bits are set in n's binary representation
        exponents = []
        # Initialize a counter for the current bit position (exponent)
        i = 0
        # Loop until n becomes 0, processing each bit
        while n:
            # Check if the least significant bit of n is 1
            if n & 1:
                # If set, append the current exponent to the list
                exponents.append(i)
            # Right-shift n by 1 to process the next bit
            n >>= 1
            # Increment the exponent counter
            i += 1
        # Get the number of set bits (length of exponents list)
        m = len(exponents)
        # Initialize a prefix sum list with m+1 zeros
        prefix = [0] * (m + 1)
        # Loop through each exponent to compute prefix sums
        for j in range(m):
            # Compute the prefix sum by adding the current exponent to the previous sum
            prefix[j + 1] = prefix[j] + exponents[j]
        # Initialize an empty list to store the answers for each query
        answers = []
        # Iterate over each query, unpacking left and right indices
        for left, right in queries:
            # Calculate the sum of exponents from left to right using prefix sums
            sum_exp = prefix[right + 1] - prefix[left]
            # Compute 2 raised to the power of sum_exp, modulo MOD
            ans = pow(2, sum_exp, MOD)
            # Append the computed answer to the answers list
            answers.append(ans)
        # Return the list of answers for all queries
        return answers

    productQueries = product_queries
