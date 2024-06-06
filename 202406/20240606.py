# https://leetcode.com/problems/hand-of-straights/


class Solution:
    """846. Hand of Straights

    Alice has some number of cards and she wants to rearrange the cards into groups so
    that each group is of size `group_size`, and consists of `group_size` consecutive
    cards.

    Given an integer array `hand` where `hand[i]` is the value written on the `ith` card
    and an integer `group_size`, return `true` if she can rearrange the cards, or
    `false` otherwise.

    """

    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool: ...

    isNStraightHand = is_n_straight_hand
