# https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements/


class Solution:
    """2163. Minimum Difference in Sums After Removal of Elements

    You are given a **0-indexed** integer array `nums` consisting of `3 * n` elements.

    You are allowed to remove any **subsequence** of elements of size **exactly** `n`
    from `nums`. The remaining `2 * n` elements will be divided into two **equal**
    parts:

    * The first `n` elements belonging to the first part and their sum is `sumfirst`.

    * The next `n` elements belonging to the second part and their sum is `sumsecond`.

    The **difference in sums** of the two parts is denoted as `sumfirst - sumsecond`.

    * For example, if `sumfirst = 3` and `sumsecond = 2`, their difference is `1`.

    * Similarly, if `sumfirst = 2` and `sumsecond = 3`, their difference is `-1`.

    Return *the **minimum difference** possible between the sums of the two parts after
    the removal of* `n` *elements*."""

    def minimum_difference(self, nums: list[int]) -> int: ...

    minimumDifference = minimum_difference
