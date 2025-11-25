# https://leetcode.com/problems/smallest-integer-divisible-by-k/


class Solution:
    """1015. Smallest Integer Divisible by K

    Given a positive integer k, you need to find the length of the smallest
    positive integer n such that n is divisible by k, and n only contains the
    digit 1.

    Return the length of n. If there is no such n, return -1.

    Note: n may not fit in a 64-bit signed integer.
    """
    def smallest_repunit_div_by_k(self, k: int) -> int:
        # Early exit: repunits are never divisible by 2 or 5
        if k % 2 == 0 or k % 5 == 0:
            return -1

        # Track current remainder of repunit mod k
        remainder = 0
        # Set of seen remainders to detect cycles
        seen = set()
        # Try lengths up to k (pigeonhole: at most k distinct remainders)
        for length in range(1, k + 1):
            # Append a '1': remainder = (remainder * 10 + 1) % k
            remainder = (remainder * 10 + 1) % k
            # If divisible by k, return length
            if remainder == 0:
                return length
            # If remainder seen before, cycle detected, impossible
            if remainder in seen:
                return -1
            # Record this remainder
            seen.add(remainder)
        # Unreachable due to pigeonhole, but safe
        return -1

    smallestRepunitDivByK = smallest_repunit_div_by_k