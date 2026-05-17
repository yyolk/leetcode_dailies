# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/


class Solution:
    """1897. Redistribute Characters to Make All Strings Equal

    You are given an array of strings `words` (**0-indexed**).

    In one operation, pick two **distinct** indices `i` and `j`, where `words[i]` is a
    non-empty string, and move **any** character from `words[i]` to **any** position in
    `words[j]`.

    Return `true` *if you can make **every** string in* `words` ***equal** using **any**
    number of operations*, *and* `false` *otherwise*.
    """

    def make_equal(self, words: list[str]) -> bool:
        n = len(words)
        concatenated = "".join(words)
        unique_chars = set(concatenated)

        # Check if the frequencies of all characters are equally distributable
        for c in unique_chars:
            if concatenated.count(c) % n != 0:
                return False
        return True

    makeEqual = make_equal
