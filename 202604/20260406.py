# https://leetcode.com/problems/walking-robot-simulation

class Solution:
    """874. Walking Robot Simulation
    
    A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot
    receives an array of integers commands, which represents a sequence of moves
    that it needs to execute. There are only three possible types of instructions
    the robot can receive: -2: Turn left 90 degrees. -1: Turn right 90 degrees. 1
    <= k <= 9: Move forward k units, one unit at a time. Some of the grid squares
    are obstacles. The i-th obstacle is at grid point obstacles[i] = (x_i, y_i).
    If the robot runs into an obstacle, it will stay in its current location (on
    the block adjacent to the obstacle) and move onto the next command. Return
    the maximum squared Euclidean distance that the robot reaches at any point in
    its path (i.e. if the distance is 5, return 25).
    
    Note: There can be an obstacle at (0, 0). The robot ignores it until moved
    off origin but cannot return due to the obstacle. North +Y, East +X,
    South -Y, West -X.
    """
    def robot_sim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # set for O(1) obstacle checks (tuples since lists are unhashable)
        obs = {tuple(o) for o in obstacles}
        # directions: 0=N(+y), 1=E(+x), 2=S(-y), 3=W(-x)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        dir_idx = 0
        max_dist = 0
        for cmd in commands:
            if cmd == -2:
                # turn left 90 degrees
                dir_idx = (dir_idx - 1) % 4
            elif cmd == -1:
                # turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            else:
                # move forward cmd units, stop before obstacle
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    nx = x + dx
                    ny = y + dy
                    if (nx, ny) in obs:
                        break
                    x, y = nx, ny
                    # update max squared Euclidean distance after each step
                    max_dist = max(max_dist, x * x + y * y)
        return max_dist

    robotSim = robot_sim