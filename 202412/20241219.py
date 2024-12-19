# https://leetcode.com/problems/max-chunks-to-make-sorted/


class Solution:
    """769. Max Chunks To Make Sorted

    You are given an integer array `arr` of length `n` that represents a permutation of
    the integers in the range `[0, n - 1]`.

    We split `arr` into some number of **chunks** (i.e., partitions), and individually
    sort each chunk. After concatenating them, the result should equal the sorted array.

    Return *the largest number of chunks we can make to sort the array*."""

    def max_chunks_to_sorted(self, arr: list[int]) -> int: ...

    maxChunksToSorted = max_chunks_to_sorted
