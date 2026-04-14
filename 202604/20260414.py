# https://leetcode.com/problems/minimum-total-distance-traveled
from collections import deque


class Solution:
    """2463. Minimum Total Distance Traveled
    
    There are some robots and factories on the X-axis. You are given an
    integer array robot where robot[i] is the position of the ith robot. You
    are also given a 2D integer array factory where factory[j] = [positionj,
    limitj] indicates that positionj is the position of the jth factory and
    that the jth factory can repair at most limitj robots. The positions of
    each robot are unique. The positions of each factory are also unique. A
    robot can be in the same position as a factory initially. All the robots
    are initially broken; they keep moving in one direction. The direction
    could be the negative or the positive direction of the X-axis. When a
    robot reaches a factory that did not reach its limit, the factory repairs
    the robot, and it stops moving. At any moment, you can set the initial
    direction of moving for some robot. Your target is to minimize the total
    distance traveled by all the robots. Return the minimum total distance
    traveled by all the robots. The test cases are generated such that all the
    robots can be repaired.
    """
    def minimum_total_distance(self, robot: list[int], factory: list[list[int]]) -> int:
        # Sort to enable ordered greedy assignment of robot suffixes to factories
        robot.sort()
        factory.sort()
        n = len(robot)
        m = len(factory)
        # dp[i][j] = min distance to repair robots[i:] using factories[j:]
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        # Base: no factories left; remaining robots impossible
        for i in range(n):
            dp[i][m] = float("inf")
        for j in range(m - 1, -1, -1):
            f_pos = factory[j][0]
            limit = factory[j][1]
            cum_dist = 0
            # Monotonic queue of (robot_idx, dp_val - cum_dist) for sliding-window min
            # within the current factory's repair limit
            mono_q = deque([(n, 0)])
            for i in range(n - 1, -1, -1):
                # Add distance of this robot (and all after it) to current factory
                cum_dist += abs(robot[i] - f_pos)
                # Evict options beyond the repair limit of this factory
                if mono_q[0][0] > i + limit:
                    mono_q.popleft()
                # Maintain decreasing order of candidate costs
                val = dp[i][j + 1] - cum_dist
                while mono_q and mono_q[-1][1] >= val:
                    mono_q.pop()
                mono_q.append((i, val))
                # Best cost using this factory for a valid suffix of robots
                dp[i][j] = mono_q[0][1] + cum_dist
        return dp[0][0]

    minimumTotalDistance = minimum_total_distance