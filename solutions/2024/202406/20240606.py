# https://leetcode.com/problems/hand-of-straights/
from collections import Counter
import heapq


class Solution:
    """846. Hand of Straights

    Alice has some number of cards and she wants to rearrange the cards into groups so
    that each group is of size `group_size`, and consists of `group_size` consecutive
    cards.

    Given an integer array `hand` where `hand[i]` is the value written on the `ith` card
    and an integer `group_size`, return `true` if she can rearrange the cards, or
    `false` otherwise.

    """

    def is_n_straight_hand(self, hand: list[int], group_size: int) -> bool:
        # If the total number of cards is not divisible by the group size, it's impossible to form groups
        if len(hand) % group_size != 0:
            return False

        # Count the frequency of each card
        count = Counter(hand)

        # Create a min-heap from the unique card values
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            # Get the smallest card value
            first = min_heap[0]

            # Try to form a group starting from the smallest card value
            for i in range(first, first + group_size):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True

    isNStraightHand = is_n_straight_hand
