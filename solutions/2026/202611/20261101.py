# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/


class Solution:
    """453. Minimum Moves to Equal Array Elements

    Given an integer array `nums` of size `n`, return *the minimum number of
    moves required to make all array elements equal*.

    In one move, you can increment `n - 1` elements of the array by `1`.

    Constraints:

    * `n == nums.length`

    * `1 <= nums.length <= 105`

    * `-109 <= nums[i] <= 109`

    * The answer is guaranteed to fit in a **32-bit** integer.
    """

    def min_moves(self, nums: list[int]) -> int:
        # Incrementing n-1 elements is equivalent to decrementing the one left out.
        # Minimum moves equals the total difference from the minimum value.
        minimum = min(nums)
        return sum(num - minimum for num in nums)

    minMoves = min_moves
