# https://leetcode.com/problems/longest-substring-of-one-repeating-character/


class Solution:
    """2213. Longest Substring of One Repeating Character

    You are given a **0-indexed** string `s`. You are also given a **0-indexed** string
    `query_characters` of length `k` and a **0-indexed** array of integer **indices**
    `query_indices` of length `k`, both of which are used to describe `k` queries.

    The `ith` query updates the character in `s` at index `query_indices[i]` to the
    character `query_characters[i]`.

    Return *an array* `lengths` *of length* `k` *where* `lengths[i]` *is the **length**
    of the **longest substring** of* `s` *consisting of **only one repeating** character
    **after** the* `ith` *query* *is performed.*

    Constraints:

    * `1 <= s.length <= 105`

    * `s` consists of lowercase English letters.

    * `k == query_characters.length == query_indices.length`

    * `1 <= k <= 105`

    * `query_characters` consists of lowercase English letters.

    * `0 <= query_indices[i] < s.length`"""

    def longest_repeating(
        self, s: str, query_characters: str, query_indices: list[int]
    ) -> list[int]:
        """...

        Proposed solution ...

        Args:
            s (str): ...
            query_characters (str): ...
            query_indices (list of int): ...

        Returns:
            list of int: ..."""
        ...

    longestRepeating = longest_repeating
