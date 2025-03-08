# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution:
    """2379. Minimum Recolors to Get K Consecutive Black Blocks

    You are given a **0-indexed** string `blocks` of length `n`, where `blocks[i]` is
    either `'W'` or `'B'`, representing the color of the `ith` block. The characters
    `'W'` and `'B'` denote the colors white and black, respectively.

    You are also given an integer `k`, which is the desired number of **consecutive**
    black blocks.

    In one operation, you can **recolor** a white block such that it becomes a black
    block.

    Return *the **minimum** number of operations needed such that there is at least
    **one** occurrence of* `k` *consecutive black blocks.*"""

    def minimum_recolors(self, blocks: str, k: int) -> int:
        min_operations = k
        n = len(blocks)

        for i in range(n - k + 1):
            min_operations = min(min_operations, blocks[i : i + k].count("W"))

        return min_operations

    minimumRecolors = minimum_recolors
