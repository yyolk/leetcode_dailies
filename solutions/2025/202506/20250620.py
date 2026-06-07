# https://leetcode.com/problems/maximum-manhattan-distance-after-k-changes/


class Solution:
    """3443. Maximum Manhattan Distance After K Changes

    You are given a string `s` consisting of the characters `'N'`, `'S'`, `'E'`, and
    `'W'`, where `s[i]` indicates movements in an infinite grid:

    * `'N'` : Move north by 1 unit.

    * `'S'` : Move south by 1 unit.

    * `'E'` : Move east by 1 unit.

    * `'W'` : Move west by 1 unit.

    Initially, you are at the origin `(0, 0)`. You can change **at most** `k` characters
    to any of the four directions.

    Find the **maximum** **Manhattan distance** from the origin that can be achieved
    **at any time** while performing the movements **in order**.

    The **Manhattan Distance** between two cells `(xi, yi)` and `(xj, yj)` is `|xi - xj|
    + |yi - yj|`."""

    def max_distance(self, s: str, k: int) -> int:
        # Initialize coordinates at origin (0, 0)
        x, y = 0, 0
        # List to store Manhattan distances at each step
        distances = []

        # Iterate through each move in the string
        for move in s:
            # Move north: increase y-coordinate
            if move == "N":
                y += 1
            # Move south: decrease y-coordinate
            elif move == "S":
                y -= 1
            # Move east: increase x-coordinate
            elif move == "E":
                x += 1
            # Move west: decrease x-coordinate
            elif move == "W":
                x -= 1
            # Calculate and store Manhattan distance (|x| + |y|)
            distances.append(abs(x) + abs(y))

        # If no changes are allowed, return maximum distance from original path
        if k == 0:
            return max(distances)

        # Initialize max distance with distance after second move
        max_dist = distances[1]
        # Store distance of previous position for comparison
        previous = distances[0]
        # Track cumulative boost from changes to maximize distance
        added_boost = 0

        # Iterate through distances starting from index 1
        for i in range(1, len(distances)):
            # Check if distance dropped and we can change a move
            if distances[i] < previous and k > 0:
                # Add boost of 2 to distance (reversing a move can increase distance by up to 2)
                added_boost += 2
                # Decrease remaining changes
                k -= 1
            # Update previous distance for next iteration
            previous = distances[i]
            # Apply cumulative boost to current distance
            distances[i] += added_boost
            # Update maximum distance seen so far
            max_dist = max(max_dist, distances[i])

        # Return the maximum Manhattan distance achievable
        return max_dist

    maxDistance = max_distance
