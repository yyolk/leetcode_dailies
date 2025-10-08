# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/


class Solution:
    """2300. Successful Pairs of Spells and Potions

    You are given two positive integer arrays `spells` and `potions`, of length `n` and
    `m` respectively, where `spells[i]` represents the strength of the `ith` spell and
    `potions[j]` represents the strength of the `jth` potion.

    You are also given an integer `success`. A spell and potion pair is considered
    **successful** if the **product** of their strengths is **at least** `success`.

    Return *an integer array* `pairs` *of length* `n` *where* `pairs[i]` *is the number
    of **potions** that will form a successful pair with the* `ith` *spell.*"""

    def successful_pairs(
        self, spells: list[int], potions: list[int], success: int
    ) -> list[int]: ...

    successfulPairs = successful_pairs
