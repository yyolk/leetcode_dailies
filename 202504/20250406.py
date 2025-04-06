# https://leetcode.com/problems/largest-divisible-subset/


class Solution:
    """368. Largest Divisible Subset

    Given a set of **distinct** positive integers `nums`, return the largest subset
    `answer` such that every pair `(answer[i], answer[j])` of elements in this subset
    satisfies:

    * `answer[i] % answer[j] == 0`, or

    * `answer[j] % answer[i] == 0`

    If there are multiple solutions, return any of them."""

    def largest_divisible_subset(self, nums: list[int]) -> list[int]: ...

    largestDivisibleSubset = largest_divisible_subset
