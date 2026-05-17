# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/


class Solution:
    """2125. Number of Laser Beams in a Bank

    Anti-theft security devices are activated inside a bank. You are given a
    **0-indexed** binary string array `bank` representing the floor plan of the bank,
    which is an `m x n` 2D matrix. `bank[i]` represents the `ith` row, consisting of
    `'0'`s and `'1'`s. `'0'` means the cell is empty, while`'1'` means the cell has a
    security device.

    There is **one** laser beam between any **two** security devices **if both**
    conditions are met:

    * The two devices are located on two **different rows**: `r1` and `r2`, where `r1 <
    r2`.

    * For **each** row `i` where `r1 < i < r2`, there are **no security devices** in the
    `ith` row.

    Laser beams are independent, i.e., one beam does not interfere nor join with
    another.

    Return *the total number of laser beams in the bank*.
    """

    def number_of_beams(self, bank: list[str]) -> int:
        # Initialize variables to keep track of the total number of laser beams (ans)
        # and the number of security devices in the previous row (temp).
        ans, temp = 0, 0

        # Iterate through each row in the bank.
        for s in bank:
            # Count the number of security devices in the current row.
            n = s.count("1")

            # If there are no security devices in the current row, continue to the next row.
            if n == 0:
                continue

            # Add the product of the number of security devices in the current row and
            # the number of security devices in the previous row to the total number
            # of laser beams.
            ans += temp * n

            # Update the variable 'temp' to store the number of security devices in the
            # current row for the next iteration.
            temp = n

        # Return the final count of laser beams.
        return ans

    numberOfBeams = number_of_beams
