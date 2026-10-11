# https://leetcode.com/problems/sum-of-squares-of-special-elements/


class Solution:
    """2778. Sum of Squares of Special Elements

    You are given a **1-indexed** integer array `nums` of length `n`.

    An element `nums[i]` of `nums` is called **special** if `i` divides `n`, i.e. `n % i
    == 0`.

    Return *the **sum of the squares** of all **special** elements of* `nums`.

    Constraints:

    * `1 <= nums.length == n <= 50`

    * `1 <= nums[i] <= 50`
    """

    def sum_of_squares(self, nums: list[int]) -> int:
        """Return the sum of squares of all special elements.

        A 1-based index i is special when it divides n.
        """
        n = len(nums)
        # Sum squares of elements whose 1-based index divides n.
        return sum(x * x for i, x in enumerate(nums, 1) if n % i == 0)

    sumOfSquares = sum_of_squares
