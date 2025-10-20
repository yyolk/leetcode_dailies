# https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
import math


class Solution:
    """1625. Lexicographically Smallest String After Applying Operations

    You are given a string `s` of **even length** consisting of digits from `0` to `9`,
    and two integers `a` and `b`.

    You can apply either of the following two operations any number of times and in any
    order on `s`:

    * Add `a` to all odd indices of `s` **(0-indexed)**. Digits post `9` are cycled back
    to `0`. For example, if `s = "3456"` and `a = 5`, `s` becomes `"3951"`.

    * Rotate `s` to the right by `b` positions. For example, if `s = "3456"` and `b =
    1`, `s` becomes `"6345"`.

    Return *the **lexicographically smallest** string you can obtain by applying the
    above operations any number of times on* `s`.

    A string `a` is lexicographically smaller than a string `b` (of the same length) if
    in the first position where `a` and `b` differ, string `a` has a letter that appears
    earlier in the alphabet than the corresponding letter in `b`. For example, `"0158"`
    is lexicographically smaller than `"0190"` because the first position they differ is
    at the third letter, and `'5'` comes before `'9'`."""

    def find_lex_smallest_string(self, s: str, a: int, b: int) -> str:
        # Compute length of s
        n = len(s)
        # Compute gcd for rotation steps
        g_rot = math.gcd(b, n)
        # Compute gcd for addition cycles
        g_add = math.gcd(a, 10)
        # Collect possible addition values mod 10
        poss_d = set((k * a) % 10 for k in range(10))
        # Initialize min_str to a large string for comparison
        min_str = "9" * n
        # Determine if rotations preserve or flip parities
        if b % 2 == 0:
            # For even b, cannot increment even positions
            for d_odd in poss_d:
                d_even = 0
                # Build modified digits with additions applied
                modified = [
                    (int(s[i]) + (d_even if i % 2 == 0 else d_odd)) % 10
                    for i in range(n)
                ]
                # Check all possible allowed rotations
                for start in range(0, n, g_rot):
                    # Construct rotated string
                    curr = "".join(str(modified[(start + j) % n]) for j in range(n))
                    # Update if smaller
                    if curr < min_str:
                        min_str = curr
        else:
            # For odd b, can increment both parity groups independently
            for d_even in poss_d:
                for d_odd in poss_d:
                    # Build modified digits with additions applied
                    modified = [
                        (int(s[i]) + (d_even if i % 2 == 0 else d_odd)) % 10
                        for i in range(n)
                    ]
                    # Check all possible allowed rotations
                    for start in range(0, n, g_rot):
                        # Construct rotated string
                        curr = "".join(str(modified[(start + j) % n]) for j in range(n))
                        # Update if smaller
                        if curr < min_str:
                            min_str = curr
        return min_str

    findLexSmallestString = find_lex_smallest_string
