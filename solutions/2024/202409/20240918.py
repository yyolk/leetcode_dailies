# https://leetcode.com/problems/largest-number/
import functools


class Solution:
    """179. Largest Number

    Given a list of non\\-negative integers `nums`, arrange them such that they form the
    largest number and return it.

    Since the result may be very large, so you need to return a string instead of an
    integer.

    """

    def largest_number(self, nums: list[int]) -> str:
        # Convert all numbers to strings for easier comparison and concatenation
        nums = [str(num) for num in nums]

        # Define a key function for sorting
        def compare(a, b):
            # If ab > ba, then a should come before b in our sorting
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort nums using the compare function
        nums.sort(key=functools.cmp_to_key(compare))

        # After sorting, if the first number is "0", then all numbers were "0"
        if nums[0] == "0":
            return "0"

        # Join all numbers to form the largest number
        return "".join(nums)

    largestNumber = largest_number
