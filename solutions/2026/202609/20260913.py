# https://leetcode.com/problems/image-overlap/

from collections import Counter


class Solution:
    """835. Image Overlap

    You are given two images, `img1` and `img2`, represented as binary, square
    matrices of size `n x n`. A binary matrix has only `0`s and `1`s as values.

    We **translate** one image however we choose by sliding all the `1` bits
    left, right, up, and/or down any number of units. We then place it on top
    of the other image. We can then calculate the **overlap** by counting the
    number of positions that have a `1` in **both** images.

    Note also that a translation does **not** include any kind of rotation.
    Any `1` bits that are translated outside of the matrix borders are erased.

    Return *the largest possible overlap*.

    Constraints:

    * `n == img1.length == img1[i].length`

    * `n == img2.length == img2[i].length`

    * `1 <= n <= 30`

    * `img1[i][j]` is either `0` or `1`.

    * `img2[i][j]` is either `0` or `1`.
    """

    def largest_overlap(self, img1: list[list[int]], img2: list[list[int]]) -> int:
        n = len(img1)
        # Ones that can still overlap after a translation
        ones1 = [(r, c) for r in range(n) for c in range(n) if img1[r][c]]
        ones2 = [(r, c) for r in range(n) for c in range(n) if img2[r][c]]
        # Each pair of ones implies a translation vector (dr, dc)
        shifts = Counter((r1 - r2, c1 - c2) for r1, c1 in ones1 for r2, c2 in ones2)
        return max(shifts.values(), default=0)

    largestOverlap = largest_overlap
