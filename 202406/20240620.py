# https://leetcode.com/problems/magnetic-force-between-two-balls/


class Solution:
    """1552. Magnetic Force Between Two Balls

    In the universe Earth C-137, Rick discovered a special form of magnetic force
    between two balls if they are put in his new invented basket. Rick has `n` empty
    baskets, the `ith` basket is at `position[i]`, Morty has `m` balls and needs to
    distribute the balls into the baskets such that the **minimum magnetic force**
    between any two balls is **maximum**.

    Rick stated that magnetic force between two different balls at positions `x` and `y`
    is `|x - y|`.

    Given the integer array `position` and the integer `m`. Return *the required force*.

    """

    def max_distance(self, position: list[int], m: int) -> int:
        # Helper function to check if it's possible to place m balls with at least min_force distance
        def can_place_balls(min_force):
            count = 1
            last_position = position[0]
            for i in range(1, len(position)):
                if position[i] - last_position >= min_force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False

        # Sort the positions to apply the greedy algorithm
        position.sort()
        # Initialize binary search bounds
        left, right = 1, position[-1] - position[0]
        result = 0

        while left <= right:
            mid = (left + right) // 2
            if can_place_balls(mid):
                result = mid  # Update result since mid is a valid minimum force
                left = mid + 1  # Try for a larger minimum force
            else:
                right = mid - 1  # Try for a smaller minimum force

        return result

    maxDistance = max_distance
