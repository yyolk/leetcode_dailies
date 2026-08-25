# https://leetcode.com/problems/smallest-missing-multiple-of-k/


class Solution:
    """3718. Smallest Missing Multiple of K

    Given an integer array `nums` and an integer `k`, return the **smallest positive
    multiple** of `k` that is **missing** from `nums`.

    A **multiple** of `k` is any positive integer divisible by `k`.

    Constraints:

    * `1 <= nums.length <= 100`

    * `1 <= nums[i] <= 100`

    * `1 <= k <= 100`"""

    def missing_multiple(self, nums: list[int], k: int) -> int:
        """Return the smallest missing positive multiple of ``k`` from ``nums``."""
        present = set(nums)
        candidate = k
        while candidate in present:
            candidate += k
        return candidate

    missingMultiple = missing_multiple
