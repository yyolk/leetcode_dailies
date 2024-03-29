# https://leetcode.com/problems/set-mismatch/


class Solution:
    """645. Set Mismatch

    You have a set of integers `s`, which originally contains all the numbers from `1`
    to `n`. Unfortunately, due to some error, one of the numbers in `s` got duplicated
    to another number in the set, which results in **repetition of one** number and
    **loss of another** number.

    You are given an integer array `nums` representing the data status of this set after
    the error.

    Find the number that occurs twice and the number that is missing and return *them in
    the form of an array*.
    """

    def find_error_nums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = set()
        duplicate = -1
        missing = -1

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        for i in range(1, n + 1):
            if i not in seen:
                missing = i

        return [duplicate, missing]

    findErrorNums = find_error_nums
