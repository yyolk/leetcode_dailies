# https://leetcode.com/problems/grumpy-bookstore-owner/


class Solution:
    """1052. Grumpy Bookstore Owner

    There is a bookstore owner that has a store open for `n` minutes. Every minute, some
    number of customers enter the store. You are given an integer array `customers` of
    length `n` where `customers[i]` is the number of the customer that enters the store
    at the start of the `ith` minute and all those customers leave after the end of that
    minute.

    On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy
    where `grumpy[i]` is `1` if the bookstore owner is grumpy during the `ith` minute,
    and is `0` otherwise.

    When the bookstore owner is grumpy, the customers of that minute are not satisfied,
    otherwise, they are satisfied.

    The bookstore owner knows a secret technique to keep themselves not grumpy for
    `minutes` consecutive minutes, but can only use it once.

    Return *the maximum number of customers that can be satisfied throughout the day*.

    """

    def max_satisfied(
        self, customers: list[int], grumpy: list[int], minutes: int
    ) -> int:
        # Calculate the number of initially satisfied customers (when the owner is not grumpy)
        total_satisfied = 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total_satisfied += customers[i]

        # Calculate the additional customers that can be satisfied using the secret technique
        # Initialize the additional satisfied customers for the first window
        max_additional_satisfied = 0
        additional_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
        max_additional_satisfied = additional_satisfied

        # Use a sliding window to find the maximum additional satisfied customers
        for i in range(minutes, len(customers)):
            if grumpy[i] == 1:
                additional_satisfied += customers[i]
            if grumpy[i - minutes] == 1:
                additional_satisfied -= customers[i - minutes]
            max_additional_satisfied = max(
                max_additional_satisfied, additional_satisfied
            )

        # The maximum number of satisfied customers is the initial satisfied customers
        # plus the maximum additional satisfied customers
        return total_satisfied + max_additional_satisfied

    maxSatisfied = max_satisfied
