# https://leetcode.com/problems/number-of-laser-beams-in-a-bank/


class Solution:
    """2125. Number of Laser Beams in a Bank

    Anti-theft security devices are activated inside a bank. You are given a
    **0-indexed** binary string array `bank` representing the floor plan of the bank,
    which is an `m x n` 2D matrix. `bank[i]` represents the `ith` row, consisting of
    `"0"`s and `"1"`s. `"0"` means the cell is empty, while`"1"` means the cell has a
    security device.

    There is **one** laser beam between any **two** security devices **if both**
    conditions are met:

    * The two devices are located on two **different rows**: `r1` and `r2`, where `r1 <
    r2`.

    * For **each** row `i` where `r1 < i < r2`, there are **no security devices** in the
    `ith` row.

    Laser beams are independent, i.e., one beam does not interfere nor join with
    another.

    Return *the total number of laser beams in the bank*."""

    def number_of_beams(self, bank: list[str]) -> int:
        # Compute the number of security devices in each row
        row_counts = [row.count("1") for row in bank]
        # Collect counts only for rows with at least one device
        devices = [count for count in row_counts if count > 0]
        # If fewer than two non-empty rows, no beams possible
        if len(devices) < 2:
            return 0
        # Initialize total number of beams
        total = 0
        # Sum products of device counts for each pair of consecutive non-empty rows
        for i in range(len(devices) - 1):
            total += devices[i] * devices[i + 1]
        return total

    numberOfBeams = number_of_beams
