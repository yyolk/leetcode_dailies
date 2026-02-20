# https://leetcode.com/problems/special-binary-string


class Solution:
    """761. Special Binary String

    Special binary strings are binary strings with the following two properties:
    - The number of 0's is equal to the number of 1's.
    - Every prefix of the binary string has at least as many 1's as 0's.

    You are given a special binary string s. A move consists of choosing two
    consecutive, non-empty, special substrings of s, and swapping them. Two
    strings are consecutive if the last character of the first string is exactly
    one index before the first character of the second string. Return the
    lexicographically largest resulting string possible after applying the
    mentioned operations on the string.
    """
    def make_largest_special(self, s: str) -> str:
        parts = []
        count = 0
        start = 0
        for i in range(len(s)):
            # Update balance: +1 for "1", -1 for "0"
            count += 1 if s[i] == "1" else -1
            if count == 0:
                # s[start:i+1] is a top-level special block
                # Recurse on inner s[start+1:i] (after outer "1" and before "0")
                inner = self.make_largest_special(s[start + 1 : i])
                block = "1" + inner + "0"
                parts.append(block)
                start = i + 1
        # Sort descending: swaps of consecutive specials allow any order
        parts.sort(reverse=True)
        return "".join(parts)

    makeLargestSpecial = make_largest_special