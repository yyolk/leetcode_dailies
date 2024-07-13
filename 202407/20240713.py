# https://leetcode.com/problems/robot-collisions/


class Solution:
    """2751. Robot Collisions

    There are `n` **1-indexed** robots, each having a position on a line, health, and
    movement direction.

    You are given **0-indexed** integer arrays `positions`, `healths`, and a string
    `directions` (`directions[i]` is either **'L'** for **left** or **'R'** for
    **right**). All integers in `positions` are **unique**.

    All robots start moving on the line **simultaneously** at the **same speed** in
    their given directions. If two robots ever share the same position while moving,
    they will **collide**.

    If two robots collide, the robot with **lower health** is **removed** from the line,
    and the health of the other robot **decreases** **by one**. The surviving robot
    continues in the **same** direction it was going. If both robots have the **same**
    health, they are bothremoved from the line.

    Your task is to determine the **health** of the robots that survive the collisions,
    in the same **order** that the robots were given,i.e. final heath of robot 1 (if
    survived), final health of robot 2 (if survived), and so on. If there are no
    survivors, return an empty array.

    Return *an array containing the health of the remaining robots (in the order they
    were given in the input), after no further collisions can occur.*

    **Note:** The positions may be unsorted.



    """

    def survived_robots_healths(
        self, positions: list[int], healths: list[int], directions: str
    ) -> list[int]:
        # Create a list of tuples (position, health, direction, index)
        robots = [(positions[i], healths[i], directions[i], i) for i in range(len(positions))]
        
        # Sort robots by their positions
        robots.sort()

        stack = []  # To keep track of robots moving to the right
        survivors = []  # To store final healths of surviving robots in the order of their original indices
        
        for pos, health, direction, index in robots:
            if direction == 'R':
                stack.append((health, index))
            else:
                while stack and stack[-1][0] < health:
                    health -= 1
                    stack.pop()
                if stack:
                    if stack[-1][0] == health:
                        stack.pop()
                    else:
                        stack[-1] = (stack[-1][0] - 1, stack[-1][1])
                else:
                    survivors.append((health, index))
        
        # Add any remaining robots from the stack (those moving to the right that never collided)
        for health, index in stack:
            survivors.append((health, index))
        
        # Sort survivors by their original indices to match the order given in input
        survivors.sort(key=lambda x: x[1])
        
        # Extract the healths in the correct order
        return [health for health, index in survivors]

    survivedRobotsHealths = survived_robots_healths
