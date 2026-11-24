# https://leetcode.com/problems/maximum-subarray-with-equal-products/

import math


class Solution:
    """3411. Maximum Subarray With Equal Products

    You are given an array of **positive** integers `nums`.

    An array `arr` is called **product equivalent** if
    `prod(arr) == lcm(arr) * gcd(arr)`, where:

    * `prod(arr)` is the product of all elements of `arr`.

    * `gcd(arr)` is the GCD of all elements of `arr`.

    * `lcm(arr)` is the LCM of all elements of `arr`.

    Return the length of the **longest** **product equivalent**
    subarray of `nums`.

    Constraints:

    * `2 <= nums.length <= 100`

    * `1 <= nums[i] <= 10`
    """

    def max_length(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        # Enumerate every subarray; n <= 100 makes O(n^2) acceptable.
        for i in range(n):
            prod = 1
            g = 0
            l = 1
            for j in range(i, n):
                prod *= nums[j]
                # Running GCD and LCM of the current subarray.
                g = math.gcd(g, nums[j])
                l = math.lcm(l, nums[j])
                # Check the product-equivalent condition.
                if prod == g * l:
                    ans = max(ans, j - i + 1)
        return ans

    maxLength = max_length
