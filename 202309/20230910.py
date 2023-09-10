# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/


class Solution:
    """1359. Count All Valid Pickup and Delivery Options

    Given `n` orders, each order consist in pickup and delivery services.

    Count all valid pickup/delivery possible sequences such that delivery(i) is always after
    of pickup(i).

    Since the answer may be too large, return it modulo 10^9 + 7.
    """

    def countOrders(self, n: int) -> int:
        """Count the valid pickup/delivery sequences

        Proposed solution using dynamic programming

        Each pickup requires a corresponding delivery, there will be one less
        order remaining for the pickup/delivery sequence.

        If it is the first delivery, then we cannot have any pickup before it.

        Args:
            n (int): the input number of orders

        Returns:
            int: the count of valid pickup/delivery sequences
        """
        # The requested ceiling to normalize our answer to
        MOD = 10**9 + 7

        # Initialize with the base case of zero orders,
        # of which, 1 is the only solution
        count = 1

        # Calculate the number of valid sequences, the number of valid pickup
        # and delivery sequences for the remaining n-1 orders will be the same
        for i in range(1, n + 1):
            count = (count * (2 * i - 1) * i) % MOD

        return count
