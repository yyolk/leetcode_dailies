# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/


class Solution:
    """2966. Divide Array Into Arrays With Max Difference

    You are given an integer array `nums` of size `n` where `n` is a multiple of 3 and a
    positive integer `k`.

    Divide the array `nums` into `n / 3` arrays of size **3** satisfying the following
    condition:

    * The difference between **any** two elements in one array is **less than or equal**
    to `k`.

    Return a **2D** array containing the arrays. If it is impossible to satisfy the
    conditions, return an empty array. And if there are multiple answers, return **any**
    of them."""

    def divide_array(self, nums: list[int], k: int) -> list[list[int]]: ...

    divideArray = divide_array
