# https://leetcode.com/problems/lexicographically-smallest-equivalent-string/


class Solution:
    """1061. Lexicographically Smallest Equivalent String

    You are given two strings of the same length `s1` and `s2` and a string `base_str`.

    We say `s1[i]` and `s2[i]` are equivalent characters.

    * For example, if `s1 = "abc"` and `s2 = "cde"`, then we have `"a" == "c"`, `"b" ==
    "d"`, and `"c" == "e"`.

    Equivalent characters follow the usual rules of any equivalence relation:

    * **Reflexivity:** `"a" == "a"`.

    * **Symmetry:** `"a" == "b"` implies `"b" == "a"`.

    * **Transitivity:** `"a" == "b"` and `"b" == "c"` implies `"a" == "c"`.

    For example, given the equivalency information from `s1 = "abc"` and `s2 = "cde"`,
    `"acd"` and `"aab"` are equivalent strings of `base_str = "eed"`, and `"aab"` is the
    lexicographically smallest equivalent string of `base_str`.

    Return *the lexicographically smallest equivalent string of* `base_str` *by using
    the equivalency information from* `s1` *and* `s2`."""

    def smallest_equivalent_string(self, s1: str, s2: str, base_str: str) -> str:
        # Initialize parent array for 26 lowercase letters, where each letter is its own parent
        parent = [i for i in range(26)]

        # Find function with path compression to get the root of a character"s group
        def find(idx: int) -> int:
            if parent[idx] != idx:
                parent[idx] = find(parent[idx])  # Path compression
            return parent[idx]

        # Process equivalencies from s1 and s2
        for i in range(len(s1)):
            # Convert characters to indices (0 for "a", 1 for "b", etc.)
            x = ord(s1[i]) - ord("a")
            y = ord(s2[i]) - ord("a")
            # Find the roots of both characters
            root_x = find(x)
            root_y = find(y)
            # Union the groups, making the smaller character the root
            if root_x != root_y:
                if root_x < root_y:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y

        # Build the result string by mapping each character in base_str to its group"s smallest character
        result = []
        for c in base_str:
            idx = ord(c) - ord("a")
            root_idx = find(idx)
            result.append(chr(root_idx + ord("a")))

        return "".join(result)

    smallestEquivalentString = smallest_equivalent_string
