# https://leetcode.com/problems/image-overlap/


class Solution:
    """835. Image Overlap

    You are given two images, `img1` and `img2`, represented as binary, square matrices
    of size `n x n`. A binary matrix has only `0`s and `1`s as values.

    We **translate** one image however we choose by sliding all the `1` bits left,
    right, up, and/or down any number of units. We then place it on top of the other
    image. We can then calculate the **overlap** by counting the number of positions
    that have a `1` in **both** images.

    Note also that a translation does **not** include any kind of rotation. Any `1` bits
    that are translated outside of the matrix borders are erased.

    Return *the largest possible overlap*.

    Constraints:

    * `n == img1.length == img1[i].length`

    * `n == img2.length == img2[i].length`

    * `1 <= n <= 30`

    * `img1[i][j]` is either `0` or `1`.

    * `img2[i][j]` is either `0` or `1`."""

    def largest_overlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        """...

        Proposed solution ...

        Args:
            img1 (list of list of int): ...
            img2 (list of list of int): ...

        Returns:
            int: ..."""
        ...

    largestOverlap = largest_overlap
