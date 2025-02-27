# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/


class Solution:
    """873. Length of Longest Fibonacci Subsequence

    A sequence `x1, x2, ..., xn` is *Fibonacci-like* if:

    * `n >= 3`

    * `xi + xi+1 == xi+2` for all `i + 2 <= n`

    Given a **strictly increasing** array `arr` of positive integers forming a sequence,
    return *the **length** of the longest Fibonacci-like subsequence of* `arr`. If one
    does not exist, return `0`.

    A **subsequence** is derived from another sequence `arr` by deleting any number of
    elements (including none) from `arr`, without changing the order of the remaining
    elements. For example, `[3, 5, 8]` is a subsequence of `[3, 4, 5, 6, 7, 8]`."""

    def len_longest_fib_subseq(self, arr: list[int]) -> int:
        n = len(arr)
        # If array length is less than 3, no Fibonacci sequence possible
        if n < 3:
            return 0
            
        # Create a set for O(1) lookup
        s = set(arr)
        # dp[(i,j)] stores length of Fibonacci sequence ending with arr[i], arr[j]
        dp = {}
        
        max_len = 0
        # Consider all possible pairs as the first two numbers
        for j in range(1, n):
            for i in range(j):
                x = arr[i]  # First number
                y = arr[j]  # Second number
                
                # The third number should be y + x
                z = x + y
                
                # If z exists in array, we can form at least length 3
                if z in s:
                    # Update the length of sequence ending with (y, z)
                    dp[(y, z)] = max(dp.get((y, z), 2), dp.get((x, y), 2) + 1)
                    max_len = max(max_len, dp[(y, z)])
        
        # Return max_len if we found any Fibonacci sequence, else 0
        return max_len if max_len >= 3 else 0

    lenLongestFibSubseq = len_longest_fib_subseq
