# https://leetcode.com/problems/palindromic-path-queries-in-a-tree/


class Solution:
    """3841. Palindromic Path Queries in a Tree

    You are given an undirected tree with `n` nodes labeled 0 to `n - 1`. This is
    represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [ui, vi]`
    indicates an undirected edge between nodes `ui` and `vi`.

    You are also given a string `s` of length `n` consisting of lowercase English
    letters, where `s[i]` represents the character assigned to node `i`.

    You are also given a string array `queries`, where each `queries[i]` is either:

    * `"update ui c"`: Change the character at node `ui` to `c`. Formally, update `s[ui]
    = c`.

    * `"query ui vi"`: Determine whether the string formed by the characters on the
    **unique** path from `ui` to `vi` (inclusive) can be **rearranged** into a
    **palindrome**.

    Return a boolean array `answer`, where `answer[j]` is `true` if the `jth` query of
    type `"query ui vi"\u200b\u200b\u200b\u200b\u200b\u200b\u200b` can be rearranged into a **palindrome**, and `false`
    otherwise.

    Constraints:

    * `1 <= n == s.length <= 5 * 104`

    * `edges.length == n - 1`

    * `edges[i] = [ui, vi]`

    * `0 <= ui, vi <= n - 1`

    * `s` consists of lowercase English letters.

    * The input is generated such that `edges` represents a valid tree.

    * `1 <= queries.length <= 5 * 104`\u200b\u200b\u200b\u200b\u200b\u200b\u200b

      + `queries[i] = "update ui c"` or

      + `queries[i] = "query ui vi"`

      + `0 <= ui, vi <= n - 1`

      + `c` is a lowercase English letter."""

    def palindrome_path(
        self, n: int, edges: list[list[int]], s: str, queries: list[str]
    ) -> list[bool]:
        """...

        Proposed solution ...

        Args:
            n (int): ...
            edges (list of list of int): ...
            s (str): ...
            queries (list of str): ...

        Returns:
            list of bool: ..."""
        ...

    palindromePath = palindrome_path
