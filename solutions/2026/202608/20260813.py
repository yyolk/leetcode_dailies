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
        """Return longest equal-char substring length after each point update."""
        n = len(s)
        arr = list(s)
        size = 1
        while size < n:
            size <<= 1

        left_char = [""] * (2 * size)
        right_char = [""] * (2 * size)
        pref = [0] * (2 * size)
        suff = [0] * (2 * size)
        best = [0] * (2 * size)
        seg_len = [0] * (2 * size)

        for i in range(n):
            idx = size + i
            char = arr[i]
            left_char[idx] = char
            right_char[idx] = char
            pref[idx] = 1
            suff[idx] = 1
            best[idx] = 1
            seg_len[idx] = 1

        for idx in range(size - 1, 0, -1):
            left_idx = idx * 2
            right_idx = left_idx + 1

            left_len = seg_len[left_idx]
            right_len = seg_len[right_idx]
            total_len = left_len + right_len
            seg_len[idx] = total_len
            if total_len == 0:
                continue

            left_char[idx] = (
                left_char[left_idx] if left_len > 0 else left_char[right_idx]
            )
            right_char[idx] = (
                right_char[right_idx] if right_len > 0 else right_char[left_idx]
            )

            pref_val = pref[left_idx]
            if left_len > 0 and pref[left_idx] == left_len and right_len > 0:
                if right_char[left_idx] == left_char[right_idx]:
                    pref_val = left_len + pref[right_idx]

            suff_val = suff[right_idx]
            if right_len > 0 and suff[right_idx] == right_len and left_len > 0:
                if right_char[left_idx] == left_char[right_idx]:
                    suff_val = right_len + suff[left_idx]

            cross = 0
            if left_len > 0 and right_len > 0:
                if right_char[left_idx] == left_char[right_idx]:
                    cross = suff[left_idx] + pref[right_idx]

            pref[idx] = pref_val
            suff[idx] = suff_val
            best[idx] = max(best[left_idx], best[right_idx], cross)

        answer: list[int] = []
        for char, pos in zip(query_characters, query_indices, strict=True):
            if arr[pos] != char:
                arr[pos] = char
                idx = size + pos
                left_char[idx] = char
                right_char[idx] = char
                pref[idx] = 1
                suff[idx] = 1
                best[idx] = 1
                idx //= 2

                while idx >= 1:
                    left_idx = idx * 2
                    right_idx = left_idx + 1

                    left_len = seg_len[left_idx]
                    right_len = seg_len[right_idx]
                    total_len = left_len + right_len
                    seg_len[idx] = total_len
                    if total_len == 0:
                        idx //= 2
                        continue

                    left_char[idx] = (
                        left_char[left_idx] if left_len > 0 else left_char[right_idx]
                    )
                    right_char[idx] = (
                        right_char[right_idx] if right_len > 0 else right_char[left_idx]
                    )

                    pref_val = pref[left_idx]
                    if left_len > 0 and pref[left_idx] == left_len and right_len > 0:
                        if right_char[left_idx] == left_char[right_idx]:
                            pref_val = left_len + pref[right_idx]

                    suff_val = suff[right_idx]
                    if right_len > 0 and suff[right_idx] == right_len and left_len > 0:
                        if right_char[left_idx] == left_char[right_idx]:
                            suff_val = right_len + suff[left_idx]

                    cross = 0
                    if left_len > 0 and right_len > 0:
                        if right_char[left_idx] == left_char[right_idx]:
                            cross = suff[left_idx] + pref[right_idx]

                    pref[idx] = pref_val
                    suff[idx] = suff_val
                    best[idx] = max(best[left_idx], best[right_idx], cross)
                    idx //= 2

            answer.append(best[1])

        return answer

    longestRepeating = longest_repeating
