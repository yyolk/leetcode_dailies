# https://leetcode.com/problems/find-polygon-with-the-largest-perimeter/


class Solution:
    """2971. Find Polygon With the Largest Perimeter

    You are given an array of **positive** integers `nums` of length `n`.

    A **polygon** is a closed plane figure that has at least `3` sides. The **longest
    side** of a polygon is **smaller** than the sum of its other sides.

    Conversely, if you have `k` (`k >= 3`) **positive** real numbers `a1`, `a2`, `a3`,
    ..., `ak` where `a1 <= a2 <= a3 <= ... <= ak` **and** `a1 + a2 + a3 + ... + ak-1 >
    ak`, then there **always** exists a polygon with `k` sides whose lengths are `a1`,
    `a2`, `a3`, ..., `ak`.

    The **perimeter** of a polygon is the sum of lengths of its sides.

    Return *the **largest** possible **perimeter** of a **polygon** whose sides can be
    formed from* `nums`, *or* `-1` *if it is not possible to create a polygon*.

    """

    def largest_perimeter(self, nums: list[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        # Initialize variables for tracking sum and answer
        sum_val = 0
        ans = -1

        # Iterate through the sorted array
        for num in nums:
            # Check if the current number can form a valid triangle
            if num < sum_val:
                # Update the answer if a valid triangle is found
                ans = num + sum_val
            # Update the sum of previous elements
            sum_val += num
            
        return ans

    largestPerimeter = largest_perimeter
