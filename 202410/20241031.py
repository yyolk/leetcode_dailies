# https://leetcode.com/problems/minimum-total-distance-traveled/
from collections import deque


class Solution:
    """2463. Minimum Total Distance Traveled

    There are some robots and factories on the X\\-axis. You are given an integer array
    `robot` where `robot[i]` is the position of the `ith` robot. You are also given a 2D
    integer array `factory` where `factory[j] = [positionj, limitj]` indicates that
    `positionj` is the position of the `jth` factory and that the `jth` factory can
    repair at most `limitj` robots.

    The positions of each robot are **unique**. The positions of each factory are also
    **unique**. Note that a robot can be **in the same position** as a factory
    initially.

    All the robots are initially broken; they keep moving in one direction. The
    direction could be the negative or the positive direction of the X\\-axis. When a
    robot reaches a factory that did not reach its limit, the factory repairs the robot,
    and it stops moving.

    **At any moment**, you can set the initial direction of moving for **some** robot.
    Your target is to minimize the total distance traveled by all the robots.

    Return *the minimum total distance traveled by all the robots*. The test cases are
    generated such that all the robots can be repaired.

    **Note that**

    * All robots move at the same speed.

    * If two robots move in the same direction, they will never collide.

    * If two robots move in opposite directions and they meet at some point, they do not
    collide. They cross each other.

    * If a robot passes by a factory that reached its limits, it crosses it as if it
    does not exist.

    * If the robot moved from a position `x` to a position `y`, the distance it moved is
    `|y - x|`.

    """

    def minimum_total_distance(
        self, robot_positions: list[int], factory_positions_and_limits: list[list[int]]
    ) -> int:
        # Sort robots and factories by their positions to optimize the matching process
        robot_positions.sort()
        factory_positions_and_limits.sort()

        total_robots, total_factories = len(robot_positions), len(
            factory_positions_and_limits
        )

        # Initialize dynamic programming table where dp[i][j] represents the minimum distance for i robots to be assigned to j factories
        dp = [[0] * (total_factories + 1) for _ in range(total_robots + 1)]

        # Base case: If there are no more factories, the distance for remaining robots is infinite
        for i in range(total_robots):
            dp[i][-1] = float("inf")

        # Iterate through factories from right to left
        for factory_index in range(total_factories - 1, -1, -1):
            cumulative_distance_to_current_factory = 0
            monotonic_queue = deque([(total_robots, 0)])

            # Iterate through robots from right to left for the current factory
            for robot_index in range(total_robots - 1, -1, -1):
                # Calculate the distance from the current robot to the current factory
                cumulative_distance_to_current_factory += abs(
                    robot_positions[robot_index]
                    - factory_positions_and_limits[factory_index][0]
                )

                # Remove entries from the queue that are out of the current factory's repair limit window
                if (
                    monotonic_queue[0][0]
                    > robot_index + factory_positions_and_limits[factory_index][1]
                ):
                    monotonic_queue.popleft()

                # Maintain the monotonic queue property where elements decrease in value
                while (
                    monotonic_queue
                    and monotonic_queue[-1][1]
                    >= dp[robot_index][factory_index + 1]
                    - cumulative_distance_to_current_factory
                ):
                    monotonic_queue.pop()

                # Add current robot's contribution to the queue
                monotonic_queue.append(
                    (
                        robot_index,
                        dp[robot_index][factory_index + 1]
                        - cumulative_distance_to_current_factory,
                    )
                )

                # Update the dp table with the minimum distance including the current factory
                dp[robot_index][factory_index] = (
                    monotonic_queue[0][1] + cumulative_distance_to_current_factory
                )

        return dp[0][0]

    minimumTotalDistance = minimum_total_distance
