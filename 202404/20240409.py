# https://leetcode.com/problems/time-needed-to-buy-tickets/


class Solution:
    """2073. Time Needed to Buy Tickets

    There are `n` people in a line queuing to buy tickets, where the `0th` person is at
    the **front** of the line and the `(n - 1)th` person is at the **back** of the line.

    You are given a **0-indexed** integer array `tickets` of length `n` where the number
    of tickets that the `ith` person would like to buy is `tickets[i]`.

    Each person takes **exactly 1 second** to buy a ticket. A person can only buy **1
    ticket at a time** and has to go back to **the end** of the line (which happens
    **instantaneously**) in order to buy more tickets. If a person does not have any
    tickets left to buy, the person will **leave** the line.

    Return *the **time taken** for the person at position* `k`***(0-indexed)****to
    finish buying tickets*.

    """

    def time_required_to_buy(self, tickets: list[int], k: int) -> int:
        total = 0

        for i, x in enumerate(tickets):
            # Calculate time for each person in the line
            if i <= k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

        return total

    timeRequiredToBuy = time_required_to_buy
