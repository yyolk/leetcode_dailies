# https://leetcode.com/problems/maximum-total-damage-with-spell-casting/


class Solution:
    """3186. Maximum Total Damage With Spell Casting

    A magician has various spells.

    You are given an array `power`, where each element represents the damage of a spell.
    Multiple spells can have the same damage value.

    It is a known fact that if a magician decides to cast a spell with a damage of
    `power[i]`, they **cannot** cast any spell with a damage of `power[i] - 2`,
    `power[i] - 1`, `power[i] + 1`, or `power[i] + 2`.

    Each spell can be cast **only once**.

    Return the **maximum** possible *total damage* that a magician can cast."""

    def maximum_total_damage(self, power: list[int]) -> int: ...

    maximumTotalDamage = maximum_total_damage
