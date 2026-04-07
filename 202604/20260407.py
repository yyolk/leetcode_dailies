# https://leetcode.com/problems/walking-robot-simulation-ii

class Robot:
    """2069. Walking Robot Simulation II

    A width x height grid is on an XY-plane with the bottom-left cell at (0, 0)
    and the top-right cell at (width - 1, height - 1). The grid is aligned with
    the four cardinal directions ("North", "East", "South", and "West"). A robot
    is initially at cell (0, 0) facing direction "East".

    The robot can be instructed to move for a specific number of steps. For each
    step, it does the following. Attempts to move forward one cell in the
    direction it is facing. If the cell the robot is moving to is out of bounds,
    the robot instead turns 90 degrees counterclockwise and retries the step.

    After the robot finishes moving the number of steps required, it stops and
    awaits the next instruction.

    Implement the Robot class:
    Robot(width, height) initializes the grid with the robot at (0, 0) facing
    "East".
    step(num) instructs the robot to move forward num steps.
    getPos() returns the current cell [x, y].
    getDir() returns the current direction string.
    """
    def __init__(self, width: int, height: int):
        # precompute positions/directions along perimeter cycle (CCW)
        # index 0 is dummy (0,0,"South") to align modulo for full cycles
        self.path = [(0, 0, "South")]
        for i in range(1, width):
            self.path.append((i, 0, "East"))
        for j in range(1, height):
            self.path.append((width - 1, j, "North"))
        for i in range(width - 2, -1, -1):
            self.path.append((i, height - 1, "West"))
        for j in range(height - 2, 0, -1):
            self.path.append((0, j, "South"))
        self.steps = 0

    def step(self, num: int) -> None:
        # accumulate total steps (handles up to 10^9 efficiently)
        self.steps += num

    def get_pos(self) -> list[int]:
        if self.steps == 0:
            return [0, 0]
        # index into precomputed cycle
        idx = self.steps % len(self.path)
        x, y, _ = self.path[idx]
        return [x, y]

    def get_dir(self) -> str:
        if self.steps == 0:
            return "East"
        idx = self.steps % len(self.path)
        _, _, direction = self.path[idx]
        return direction

    getPos = get_pos
    getDir = get_dir