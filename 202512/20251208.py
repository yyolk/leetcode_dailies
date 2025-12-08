# https://leetcode.com/problems/count-square-sum-triples


class Solution:
    """1925. Count Square Sum Triples

    A square triple (a,b,c) is a triple where a, b, and c are integers
    and a^2 + b^2 = c^2.

    Given an integer n, return the number of square triples such that
    1 <= a, b, c <= n.
    """
    def count_triples(self, n: int) -> int:
        # Precompute set of perfect squares from 1^2 to n^2 for O(1) lookups
        squares = {i * i for i in range(1, n + 1)}
        # Initialize counter for valid triples
        count = 0
        # Iterate over all possible values of a and b
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                # Compute sum of squares
                s = a * a + b * b
                # If s is a perfect square (i.e., some c^2 with c <= n), increment count
                if s in squares:
                    count += 1
        return count

    countTriples = count_triples