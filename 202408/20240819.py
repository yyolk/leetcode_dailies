# https://leetcode.com/problems/2-keys-keyboard/


class Solution:
    """650. 2 Keys Keyboard

    There is only one character `'A'` on the screen of a notepad. You can perform one of
    two operations on this notepad for each step:

    * Copy All: You can copy all the characters present on the screen (a partial copy is
    not allowed).

    * Paste: You can paste the characters which are copied last time.

    Given an integer `n`, return *the minimum number of operations to get the character*
    `'A'` *exactly* `n` *times on the screen*.

    """

    def min_steps(self, n: int) -> int:
        # Initialize the total number of operations
        steps = 0

        # Try dividing n by every number starting from 2 onwards
        divisor = 2

        while n > 1:
            while n % divisor == 0:
                # If n is divisible by the current divisor,
                # then add the divisor to the steps and divide n by the divisor.
                steps += divisor
                n //= divisor
            divisor += 1

        return steps

    minSteps = min_steps
