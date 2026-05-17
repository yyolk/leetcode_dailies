# https://leetcode.com/problems/maximum-distance-in-arrays/


class Solution:
    """624. Maximum Distance in Arrays

    You are given `m` `arrays`, where each array is sorted in **ascending order**.

    You can pick up two integers from two different arrays (each array picks one) and
    calculate the distance. We define the distance between two integers `a` and `b` to
    be their absolute difference `|a - b|`.

    Return *the maximum distance*.

    """

    def max_distance(self, arrays: list[list[int]]) -> int:
        # Initialize the result and the minimum and maximum values
        result = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]

        # Iterate through the arrays starting from the second one
        for i in range(1, len(arrays)):
            # Calculate the distance by comparing the current array's max and min with the global min and max
            result = max(
                result, abs(arrays[i][-1] - min_val), abs(arrays[i][0] - max_val)
            )

            # Update the global min and max values
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return result

    maxDistance = max_distance
