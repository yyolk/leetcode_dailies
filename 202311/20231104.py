# https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/


class Solution:
    """1503. Last Moment Before All Ants Fall Out of a Plank

    We have a wooden plank of the length `n` **units**. Some ants are walking on the
    plank, each ant moves with a speed of **1 unit per second**. Some of the ants move
    to the **left**, the other move to the **right**.

    When two ants moving in two **different** directions meet at some point, they change
    their directions and continue moving again. Assume changing directions does not take
    any additional time.

    When an ant reaches **one end** of the plank at a time `t`, it falls out of the
    plank immediately.

    Given an integer `n` and two integer arrays `left` and `right`, the positions of the
    ants moving to the left and the right, return *the moment when the last ant(s) fall
    out of the plank*.
    """

    def get_last_moment(self, n: int, left: list[int], right: list[int]) -> int:
        """Calculate the moment when the last ant(s) fall out of the plank.

        Args:
            n: The length of the plank in units.
            left: Positions of ants moving to the left.
            right: Positions of ants moving to the right.

        Returns:
            The moment when the last ant(s) fall out of the plank.
        """
        # Calculate the time for ants moving left to fall out of the plank
        left_time = 0
        for position in left:
            left_time = max(left_time, position)

        # Calculate the time for ants moving right to fall out of the plank
        right_time = 0
        for position in right:
            right_time = max(right_time, n - position)

        # The moment when the last ant(s) fall out of the plank is the maximum of
        # either side.
        return max(left_time, right_time)

    getLastMoment = get_last_moment
