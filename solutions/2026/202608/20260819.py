# https://leetcode.com/problems/cinema-seat-allocation/


class Solution:
    """1386. Cinema Seat Allocation

    ![](https://assets.leetcode.com/uploads/2020/02/14/cinema_seats_1.png)

    A cinema has `n` rows of seats, numbered from 1 to `n`. Each row has 10 seats,
    numbered from 1 to 10.

    You are given a 2D integer array `reserved_seats`, where `reserved_seats[i] = [rowi,
    seati]` means that seat `seati` in row `rowi` is already reserved.

    A four-person group must be assigned to four seats in the **same** row. The group
    can be seated in one of the following seat blocks:

    * seats `2, 3, 4, 5`

    * seats `4, 5, 6, 7`

    * seats `6, 7, 8, 9`

    A block can be used only if **none** of its seats are reserved. Each seat can be
    assigned to **at most** one group.

    Return an integer denoting the **maximum** number of four-person groups that can be
    assigned.

    Constraints:

    * `1 <= n <= 109`

    * `1 <= reserved_seats.length <= min(10 * n, 104)`

    * `reserved_seats[i] == [rowi, seati]`

    * `1 <= rowi <= n`

    * `1 <= seati <= 10`

    * All `reserved_seats[i]` are distinct."""

    def max_number_of_families(self, n: int, reserved_seats: list[list[int]]) -> int:
        """Return the maximum number of four-person groups that can be seated."""
        blocked_by_row: dict[int, int] = {}
        for row, seat in reserved_seats:
            if 2 <= seat <= 9:
                blocked_by_row[row] = blocked_by_row.get(row, 0) | (1 << (seat - 2))

        left_block = 0b00001111  # seats 2-5
        middle_block = 0b00111100  # seats 4-7
        right_block = 0b11110000  # seats 6-9

        families = (n - len(blocked_by_row)) * 2
        for blocked in blocked_by_row.values():
            left_free = (blocked & left_block) == 0
            right_free = (blocked & right_block) == 0
            if left_free and right_free:
                families += 2
            elif left_free or right_free or (blocked & middle_block) == 0:
                families += 1

        return families

    maxNumberOfFamilies = max_number_of_families
