# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/


class Solution:
    """1743. Restore the Array From Adjacent Pairs

    There is an integer array `nums` that consists of `n` **unique** elements, but you
    have forgotten it. However, you do remember every pair of adjacent elements in
    `nums`.

    You are given a 2D integer array `adjacent_pairs` of size `n - 1` where each
    `adjacent_pairs[i] = [ui, vi]` indicates that the elements `ui` and `vi` are
    adjacent in `nums`.

    It is guaranteed that every adjacent pair of elements `nums[i]` and `nums[i+1]` will
    exist in `adjacent_pairs`, either as `[nums[i], nums[i+1]]` or `[nums[i+1],
    nums[i]]`. The pairs can appear **in any order**.

    Return *the original array* `nums`*. If there are multiple solutions, return **any
    of them***.
    """

    def restore_array(self, adjacent_pairs: List[List[int]]) -> List[int]:
        ...

    restoreArray = restore_array
