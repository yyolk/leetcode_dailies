# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/


class Solution:
    """1578. Minimum Time to Make Rope Colorful

    Alice has `n` balloons arranged on a rope. You are given a **0-indexed** string
    `colors` where `colors[i]` is the color of the `ith` balloon.

    Alice wants the rope to be **colorful**. She does not want **two consecutive
    balloons** to be of the same color, so she asks Bob for help. Bob can remove some
    balloons from the rope to make it **colorful**. You are given a **0-indexed**
    integer array `needed_time` where `needed_time[i]` is the time (in seconds) that Bob
    needs to remove the `ith` balloon from the rope.

    Return *the **minimum time** Bob needs to make the rope **colorful***.
    """

    def min_cost(self, colors: str, needed_time: list[int]) -> int:
        start, consecutive_count, total = 0, 1, 0
        current_sum = needed_time[0]
        max_time = needed_time[0]

        # Iterate through the balloons.
        for i in range(1, len(colors)):
            # Check if the current balloon has the same color as the previous one.
            if colors[i] == colors[i - 1]:
                # If consecutive balloons have the same color, update variables.
                consecutive_count += 1
                current_sum += needed_time[i]
                max_time = max(max_time, needed_time[i])
            else:
                # If a different color is encountered, calculate the total time for
                # consecutive balloons with the same color.
                if consecutive_count > 1:
                    total += current_sum - max_time

                # Reset variables for the new color.
                consecutive_count = 1
                start = i
                current_sum = needed_time[i]
                max_time = needed_time[i]

        # Calculate the total time for the last set of consecutive balloons, if any.
        if consecutive_count > 1:
            total += current_sum - max_time

        return total

    minCost = min_cost
