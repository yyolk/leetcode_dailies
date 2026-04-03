# https://leetcode.com/problems/maximum-walls-destroyed-by-robots

from bisect import bisect_left

class Solution:
    """3661. Maximum Walls Destroyed by Robots
    
    There is an endless straight line populated with some robots and walls.
    You are given integer arrays robots, distance, and walls: robots[i] is
    the position of the ith robot. distance[i] is the maximum distance the
    ith robot's bullet can travel. walls[j] is the position of the jth wall.
    Every robot has one bullet that can either fire to the left or the right
    at most distance[i] meters. A bullet destroys every wall in its path
    that lies within its range. Robots are fixed obstacles: if a bullet hits
    another robot before reaching a wall, it immediately stops at that robot
    and cannot continue. Return the maximum number of unique walls that can
    be destroyed by the robots.
    
    Notes: A wall and a robot may share the same position; the wall can be
    destroyed by the robot at that position. Robots are not destroyed by
    bullets.
    """
    def max_walls(self, robots: list[int], distance: list[int], walls: list[int]) -> int:
        n = len(robots)
        # pair robot positions with distances; sort by position (robots unique)
        arr = sorted(zip(robots, distance))
        # sort walls once for O(log m) range counts via binary search
        wall_pos = sorted(walls)
        
        # prev_dp[0/1] holds max walls for robots processed so far when the
        # "next-robot direction" parameter for the prior state was left/right
        prev_dp = [0, 0]
        
        for i in range(n):
            pos, dist = arr[i]
            # left-fire range: clipped by previous robot (if any) to avoid overlap
            left_pos = pos - dist
            if i > 0:
                left_pos = max(left_pos, arr[i - 1][0] + 1)
            # count walls in [left_pos, pos] inclusive using bisect
            l_idx = bisect_left(wall_pos, left_pos)
            r_idx = bisect_left(wall_pos, pos + 1)
            left_cnt = r_idx - l_idx
            
            new_dp = [0] * 2
            for j in range(2):
                # right-fire range: own distance clipped by next robot
                # (depends on j = assumed direction of next robot to partition
                # inter-robot gap walls without double-counting)
                right_pos = pos + dist
                if i + 1 < n:
                    npos, ndist = arr[i + 1]
                    if j == 0:  # next fires left
                        right_pos = min(right_pos, npos - ndist - 1)
                    else:
                        right_pos = min(right_pos, npos - 1)
                # count walls in [pos, right_pos] inclusive
                l_idx = bisect_left(wall_pos, pos)
                r_idx = bisect_left(wall_pos, right_pos + 1)
                right_cnt = r_idx - l_idx
                # choose left (pass dir 0 to prior) or right (pass dir 1)
                # for this assumed next direction j
                new_dp[j] = max(left_cnt + prev_dp[0], right_cnt + prev_dp[1])
            prev_dp = new_dp
        
        # final answer uses fictional next robot firing right (j = 1)
        return prev_dp[1]

    maxWalls = max_walls