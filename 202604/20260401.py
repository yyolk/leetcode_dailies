# https://leetcode.com/problems/robot-collisions

class Solution:
    """2751. Robot Collisions
    
    There are n 1-indexed robots, each having a position on a line, health,
    and movement direction. You are given 0-indexed integer arrays positions,
    healths, and a string directions (directions[i] is either 'L' for left or
    'R' for right). All integers in positions are unique.
    
    All robots start moving on the line simultaneously at the same speed in
    their given directions. If two robots ever share the same position while
    moving, they will collide.
    
    If two robots collide, the robot with lower health is removed from the
    line, and the health of the other robot decreases by one. The surviving
    robot continues in the same direction it was going. If both robots have
    the same health, they are both removed from the line.
    
    Return an array containing the health of the remaining robots (in the
    order they were given in the input), after no further collisions can
    occur. Note: The positions may be unsorted.
    """
    def survived_robots_healths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        # sort indices by position (left to right processing order)
        indices = list(range(n))
        indices.sort(key=lambda i: positions[i])
        # stack holds original indices of active right-moving robots
        stack = []
        for curr in indices:
            if directions[curr] == "R":
                # right-mover added; may collide with future left-movers
                stack.append(curr)
            else:
                # left-mover: resolve collisions from rightmost previous R
                while stack and healths[curr] > 0:
                    top = stack.pop()
                    if healths[top] > healths[curr]:
                        # R stronger: L destroyed, R health -= 1 and stays active
                        healths[top] -= 1
                        healths[curr] = 0
                        stack.append(top)
                    elif healths[top] < healths[curr]:
                        # L stronger: R destroyed, L health -= 1 (continue fighting)
                        healths[curr] -= 1
                        healths[top] = 0
                    else:
                        # equal health: both destroyed
                        healths[curr] = 0
                        healths[top] = 0
        # return surviving healths (in original order) by filtering zeros
        return [h for h in healths if h > 0]

    survivedRobotsHealths = survived_robots_healths