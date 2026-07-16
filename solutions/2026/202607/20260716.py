# https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/


class Solution:
    """3867. Sum of GCD of Formed Pairs

    You are given an integer array `nums` of length `n`.

    Construct an array `prefixGcd` where for each index `i`:

    * Let `mxi = max(nums[0], nums[1], ..., nums[i])`.

    * `prefixGcd[i] = gcd(nums[i], mxi)`.

    After constructing `prefixGcd`:

    * Sort `prefixGcd` in **non-decreasing** order.

    * Form pairs by taking the **smallest unpaired** element and the **largest
    unpaired** element.

    * Repeat this process until no more pairs can be formed.

    * For each formed pair, **compute** the `gcd` of the two elements.

    * If `n` is odd, the **middle** element in the `prefixGcd` array remains
    **unpaired** and should be ignored.

    Return an integer denoting the **sum of the GCD** values of all formed pairs.

    The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.

    Constraints:

    * `1 <= n == nums.length <= 105`

    * `1 <= nums[i] <= 10\u200b\u200b\u200b\u200b\u200b\u200b\u200b9`"""

    def gcd_sum(self, nums: list[int]) -> int: ...

    gcdSum = gcd_sum
