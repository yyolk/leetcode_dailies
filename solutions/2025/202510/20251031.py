# https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/


class Solution:
    """3289. The Two Sneaky Numbers of Digitville

    In the town of Digitville, there was a list of numbers called `nums` containing
    integers from `0` to `n - 1`. Each number was supposed to appear **exactly once** in
    the list, however, **two** mischievous numbers sneaked in an *additional time*,
    making the list longer than usual.

    As the town detective, your task is to find these two sneaky numbers. Return an
    array of size **two** containing the two numbers (in *any order*), so peace can
    return to Digitville."""

    def get_sneaky_numbers(self, nums: list[int]) -> list[int]:
        # Initialize a set to track seen numbers
        seen = set()
        # List to hold the duplicate numbers
        result = []
        # Iterate through each number in the list
        for num in nums:
            # Check if the number is already in the seen set
            if num in seen:
                # If seen, it's a duplicate; add to result
                result.append(num)
            else:
                # Otherwise, add to seen set
                seen.add(num)
        # Return the list of duplicates
        return result

    getSneakyNumbers = get_sneaky_numbers
