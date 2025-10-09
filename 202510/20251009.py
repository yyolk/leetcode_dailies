# https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/


class Solution:
    """3494. Find the Minimum Amount of Time to Brew Potions

    You are given two integer arrays, `skill` and `mana`, of length `n` and `m`,
    respectively.

    In a laboratory, `n` wizards must brew `m` potions *in order*. Each potion has a
    mana capacity `mana[j]` and **must** pass through **all** the wizards sequentially
    to be brewed properly. The time taken by the `ith` wizard on the `jth` potion is
    `timeij = skill[i] * mana[j]`.

    Since the brewing process is delicate, a potion **must** be passed to the next
    wizard immediately after the current wizard completes their work. This means the
    timing must be *synchronized* so that each wizard begins working on a potion
    **exactly** when it arrives. \u200b

    Return the **minimum** amount of time required for the potions to be brewed
    properly."""

    def min_time(self, skill: list[int], mana: list[int]) -> int: ...

    minTime = min_time
