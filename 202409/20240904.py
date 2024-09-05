# https://leetcode.com/problems/walking-robot-simulation/


class Solution:
    """874. Walking Robot Simulation

    A robot on an infinite XY\\-plane starts at point `(0, 0)` facing north. The robot
    can receive a sequence of these three possible types of `commands`:

    * `-2`: Turn left `90` degrees.

    * `-1`: Turn right `90` degrees.

    * `1 <= k <= 9`: Move forward `k` units, one unit at a time.

    Some of the grid squares are `obstacles`. The `ith` obstacle is at grid point
    `obstacles[i] = (xi, yi)`. If the robot runs into an obstacle, then it will instead
    stay in its current location and move on to the next command.

    Return *the **maximum Euclidean distance** that the robot ever gets from the origin
    **squared** (i.e. if the distance is* `5`*, return* `25`*)*.

    **Note:**

    * North means \\+Y direction.

    * East means \\+X direction.

    * South means \\-Y direction.

    * West means \\-X direction.

    * There can be obstacle in \\[0,0].

    """

    def robot_sim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Directions: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Convert obstacles to a set for O(1) lookup time
        obstacleSet = set(map(tuple, obstacles))
        x, y = 0, 0  # Starting position
        dir_index = 0  # Start facing North
        max_distance = 0

        for command in commands:
            if command == -2:  # Turn left
                dir_index = (dir_index - 1) % 4
            elif command == -1:  # Turn right
                dir_index = (dir_index + 1) % 4
            else:  # Move forward command units
                for _ in range(command):
                    if (
                        x + directions[dir_index][0],
                        y + directions[dir_index][1],
                    ) not in obstacleSet:
                        x += directions[dir_index][0]
                        y += directions[dir_index][1]
                        # Update max distance if necessary
                        max_distance = max(max_distance, x * x + y * y)
                    else:
                        # If there's an obstacle, stop moving in this direction
                        break

        return max_distance

    robotSim = robot_sim
