# https://leetcode.com/problems/reveal-cards-in-increasing-order/
from collections import deque


class Solution:
    """950. Reveal Cards In Increasing Order

    You are given an integer array `deck`. There is a deck of cards where every card has
    a unique integer. The integer on the `ith` card is `deck[i]`.

    You can order the deck in any order you want. Initially, all the cards start face
    down (unrevealed) in one deck.

    You will do the following steps repeatedly until all cards are revealed:

    1. Take the top card of the deck, reveal it, and take it out of the deck.

    2. If there are still cards in the deck then put the next top card of the deck at
    the bottom of the deck.

    3. If there are still unrevealed cards, go back to step 1. Otherwise, stop.

    Return *an ordering of the deck that would reveal the cards in increasing order*.

    **Note** that the first entry in the answer is considered to be the top of the deck.

    """

    def deck_revealed_increasing(self, deck: list[int]) -> list[int]:
        # Sort the deck in increasing order (ascending)
        deck.sort(
            reverse=True
        )  # Descending order to simulate the reversed revealing process

        # Initialize a deque to simulate the card revealing process
        dq = deque()
        n = len(deck)
        # Start with the largest card at the bottom of the deck
        dq.appendleft(deck[0])

        # Simulate the card revealing process
        for i in range(1, n):
            # Move the top card to the bottom and then reveal the next card
            x = dq.pop()
            dq.appendleft(x)
            dq.appendleft(deck[i])

        # Collect the revealed cards in the correct order
        ans = []
        while dq:
            ans.append(dq.popleft())
        return ans

    deckRevealedIncreasing = deck_revealed_increasing
