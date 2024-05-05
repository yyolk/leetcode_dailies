# https://leetcode.com/problems/boats-to-save-people/


class Solution:
    """881. Boats to Save People

    You are given an array `people` where `people[i]` is the weight of the `ith` person,
    and an **infinite number of boats** where each boat can carry a maximum weight of
    `limit`. Each boat carries at most two people at the same time, provided the sum of
    the weight of those people is at most `limit`.

    Return *the minimum number of boats to carry every given person*.

    """

    def num_rescue_boats(self, people: list[int], limit: int) -> int:
        # Sort the people by weight
        people.sort()
        # Initialize variables for boat count and two pointers for the heaviest and lightest person
        boats = 0
        left, right = 0, len(people) - 1
        # Iterate until the pointers meet
        while left <= right:
            # Check if the heaviest and lightest person can fit in a boat
            if people[left] + people[right] <= limit:
                # Move the lighter person to the next boat
                left += 1
            # Move the heavier person to the next boat
            right -= 1
            # Increment boat count for each boat needed
            boats += 1
        return boats

    numRescueBoats = num_rescue_boats
