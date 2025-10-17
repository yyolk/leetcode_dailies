# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/


class Solution:
    """3003. Maximize the Number of Partitions After Operations

    You are given a string `s` and an integer `k`.

    First, you are allowed to change **at most** **one** index in `s` to another
    lowercase English letter.

    After that, do the following partitioning operation until `s` is **empty**:

    * Choose the **longest** **prefix** of `s` containing at most `k` **distinct**
    characters.

    * **Delete** the prefix from `s` and increase the number of partitions by one. The
    remaining characters (if any) in `s` maintain their initial order.

    Return an integer denoting the **maximum** number of resulting partitions after the
    operations by optimally choosing at most one index to change."""

    def max_partitions_after_operations(self, s: str, k: int) -> int: ...

    maxPartitionsAfterOperations = max_partitions_after_operations
