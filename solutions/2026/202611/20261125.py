# https://leetcode.com/problems/smallest-unique-subarray/


class Solution:
    """3934. Smallest Unique Subarray

    You are given an integer array nums.

    Find the minimum length of a subarray that is not identical to any other
    subarray in nums.

    Return an integer denoting the minimum possible length of such a subarray.

    Two subarrays are considered identical if they have the same length and the
    same elements in corresponding positions.

    Constraints:

    * 1 <= nums.length <= 10**5

    * 1 <= nums[i] <= 10**5
    """

    def smallest_unique_subarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        # Use rolling hash with base > max possible value for collision resistance.
        base = 131
        mod = 10**9 + 7

        # Precompute powers and prefix hashes for O(1) subarray hashes.
        powers = [1] * (n + 1)
        prefix = [0] * (n + 1)
        for i in range(n):
            powers[i + 1] = (powers[i] * base) % mod
            prefix[i + 1] = (prefix[i] * base + nums[i]) % mod

        def has_unique(length: int) -> bool:
            # Frequency map of hashes for all windows of this length.
            counts: dict[int, int] = {}
            for i in range(n - length + 1):
                # Compute hash of nums[i : i + length].
                h = (prefix[i + length] - prefix[i] * powers[length]) % mod
                counts[h] = counts.get(h, 0) + 1
            # True if any window appears exactly once.
            return any(count == 1 for count in counts.values())

        # Binary search the minimal length that has at least one unique subarray.
        # Monotonic: if length L has a unique, then every larger length does too.
        low, high = 1, n
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if has_unique(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    smallestUniqueSubarray = smallest_unique_subarray
