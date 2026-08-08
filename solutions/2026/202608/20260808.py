# https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/


class Solution:
    """3302. Find the Lexicographically Smallest Valid Sequence

    You are given two strings `word1` and `word2`.

    A string `x` is called **almost equal** to `y` if you can change **at most** one
    character in `x` to make it *identical* to `y`.

    A sequence of indices `seq` is called **valid** if:

    * The indices are sorted in **ascending** order.

    * *Concatenating* the characters at these indices in `word1` in **the same** order
    results in a string that is **almost equal** to `word2`.

    Return an array of size `word2.length` representing the lexicographically smallest
    **valid** sequence of indices. If no such sequence of indices exists, return an
    **empty** array.

    **Note** that the answer must represent the *lexicographically smallest array*,
    **not** the corresponding string formed by those indices.

    Constraints:

    * `1 <= word2.length < word1.length <= 3 * 105`

    * `word1` and `word2` consist only of lowercase English letters."""

    def valid_sequence(self, word1: str, word2: str) -> list[int]:
        """Return the lexicographically smallest valid sequence of indices.

        Let `a0[i]` be the smallest `j` such that `word2[j:]` can be matched as an exact
        subsequence of `word1[i:]`. Let `a1[i]` be the smallest `j` such that `word2[j:]`
        can be matched with at most one mismatch.

        These arrays are computed right-to-left using position lists in `word2`.
        Then we build the answer greedily from left to right, always taking the earliest
        index that still allows completion.
        """
        from bisect import bisect_left

        n = len(word1)
        m = len(word2)

        positions = [[] for _ in range(26)]
        for idx, ch in enumerate(word2):
            positions[ord(ch) - ord("a")].append(idx)

        def first_ge(pos_list: list[int], value: int) -> int:
            k = bisect_left(pos_list, value)
            return pos_list[k] if k < len(pos_list) else m + 1

        a0 = [0] * (n + 1)
        a1 = [0] * (n + 1)
        a0[n] = m
        a1[n] = m

        for i in range(n - 1, -1, -1):
            char_idx = ord(word1[i]) - ord("a")

            best0 = a0[i + 1]
            need0 = max(0, a0[i + 1] - 1)
            found0 = first_ge(positions[char_idx], need0)
            if found0 < best0:
                best0 = found0
            a0[i] = best0

            best1 = a1[i + 1]
            need1 = max(0, a1[i + 1] - 1)
            found1 = first_ge(positions[char_idx], need1)
            if found1 < best1:
                best1 = found1
            if a0[i + 1] > 0:
                mismatch_pick = a0[i + 1] - 1
                if mismatch_pick < best1:
                    best1 = mismatch_pick
            a1[i] = best1

        ans: list[int] = []
        j = 0
        mismatch_used = False

        for i, ch in enumerate(word1):
            if j == m:
                break
            if mismatch_used:
                if ch == word2[j] and j + 1 >= a0[i + 1]:
                    ans.append(i)
                    j += 1
            else:
                if ch == word2[j] and j + 1 >= a1[i + 1]:
                    ans.append(i)
                    j += 1
                elif j + 1 >= a0[i + 1]:
                    ans.append(i)
                    j += 1
                    mismatch_used = True

        return ans if j == m else []

    validSequence = valid_sequence
