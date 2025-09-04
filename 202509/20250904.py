# https://leetcode.com/problems/find-closest-person/


class Solution:
    """3516. Find Closest Person

    You are given three integers `x`, `y`, and `z`, representing the positions of three
    people on a number line:

    * `x` is the position of Person 1.

    * `y` is the position of Person 2.

    * `z` is the position of Person 3, who does **not** move.

    Both Person 1 and Person 2 move toward Person 3 at the **same** speed.

    Determine which person reaches Person 3 **first**:

    * Return 1 if Person 1 arrives first.

    * Return 2 if Person 2 arrives first.

    * Return 0 if both arrive at the **same** time.

    Return the result accordingly."""

    def find_closest(self, x: int, y: int, z: int) -> int:
        # Calculate absolute distance from Person 1 to Person 3
        dist1 = abs(x - z)
        # Calculate absolute distance from Person 2 to Person 3
        dist2 = abs(y - z)
        # Compare distances: smaller distance means arrives first since speeds are equal
        if dist1 < dist2:
            return 1
        elif dist2 < dist1:
            return 2
        else:
            # Distances equal, so arrive at same time
            return 0

    findClosest = find_closest
