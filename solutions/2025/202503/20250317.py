# https://leetcode.com/problems/divide-array-into-equal-pairs/
from collections import Counter


class Solution:
    """2206. Divide Array Into Equal Pairs

    You are given an integer array `nums` consisting of `2 * n` integers.

    You need to divide `nums` into `n` pairs such that:

    * Each element belongs to **exactly one** pair.

    * The elements present in a pair are **equal**.

    Return `true` *if nums can be divided into* `n` *pairs, otherwise return* `false`.
    """

    def divide_array(self, nums: list[int]) -> bool:
        # Count the frequency of each number in the array
        counter = Counter(nums)

        # Check if all frequencies are even
        return all(count % 2 == 0 for count in counter.values())

    divideArray = divide_array
