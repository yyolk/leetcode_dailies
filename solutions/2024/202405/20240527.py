# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/


class Solution:
    """1608. Special Array With X Elements Greater Than or Equal X

    You are given an array `nums` of non-negative integers. `nums` is considered
    **special** if there exists a number `x` such that there are **exactly** `x` numbers
    in `nums` that are **greater than or equal to** `x`.

    Notice that `x` **does not** have to be an element in `nums`.

    Return `x` *if the array is **special**, otherwise, return* `-1`. It can be proven
    that if `nums` is special, the value for `x` is **unique**.

    """

    def special_array(self, nums: list[int]) -> int:
        # Sort the array in non-decreasing order
        nums.sort()

        # Get the length of the array
        n = len(nums)

        # Iterate through possible values of x from 0 to n
        for x in range(n + 1):
            # Calculate the number of elements greater than or equal to x
            count = sum(1 for num in nums if num >= x)

            # If the count equals x, then x is our answer
            if count == x:
                return x

        # If no such x is found, return -1
        return -1

    specialArray = special_array
