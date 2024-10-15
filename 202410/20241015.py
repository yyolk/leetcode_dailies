# https://leetcode.com/problems/separate-black-and-white-balls/


class Solution:
    """2938. Separate Black and White Balls

    There are `n` balls on a table, each ball has a color black or white.

    You are given a **0\\-indexed** binary string `s` of length `n`, where `1` and `0`
    represent black and white balls, respectively.

    In each step, you can choose two adjacent balls and swap them.

    Return *the **minimum** number of steps to group all the black balls to the right
    and all the white balls to the left*.

    """

    def minimum_steps(self, s: str) -> int:
        """
        Calculate the minimum number of adjacent swaps needed to group all black balls (1's) to the right.

        This method works by counting how many white balls (0's) are encountered
        as we scan from left to right since each white ball to the left of any black ball
        will need to be swapped at least once to get all black balls to the right.

        Args:
        s: A string representing the sequence of balls where '0' is white and '1' is black.

        Returns:
        The minimum number of steps required.

        Example:
        >>> sol = Solution()
        >>> sol.minimum_steps("10101")
        3
        """
        steps = 0
        black_balls_encountered = 0
        
        # Count each white ball that appears before black balls
        for char in s:
            if char == "1":
                black_balls_encountered += 1
            elif char == "0":
                # For each white ball, we need as many steps as there are black balls to its right
                steps += black_balls_encountered
        
        return steps

    minimumSteps = minimum_steps
