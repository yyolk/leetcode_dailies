# https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/


class Solution:
    """1298. Maximum Candies You Can Get from Boxes

    You have `n` boxes labeled from `0` to `n - 1`. You are given four arrays: `status`,
    `candies`, `keys`, and `contained_boxes` where:

    * `status[i]` is `1` if the `ith` box is open and `0` if the `ith` box is closed,

    * `candies[i]` is the number of candies in the `ith` box,

    * `keys[i]` is a list of the labels of the boxes you can open after opening the
    `ith` box.

    * `contained_boxes[i]` is a list of the boxes you found inside the `ith` box.

    You are given an integer array `initial_boxes` that contains the labels of the boxes
    you initially have. You can take all the candies in **any open box** and you can use
    the keys in it to open new boxes and you also can use the boxes you find in it.

    Return *the maximum number of candies you can get following the rules above*."""

    def max_candies(
        self,
        status: list[int],
        candies: list[int],
        keys: list[list[int]],
        contained_boxes: list[list[int]],
        initial_boxes: list[int],
    ) -> int: ...

    maxCandies = max_candies
