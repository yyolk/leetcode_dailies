# https://leetcode.com/problems/find-k-th-smallest-pair-distance/


class Solution:
    """719. Find K-th Smallest Pair Distance

    The **distance of a pair** of integers `a` and `b` is defined as the absolute
    difference between `a` and `b`.

    Given an integer array `nums` and an integer `k`, return *the* `kth` *smallest
    **distance among all the pairs*** `nums[i]` *and* `nums[j]` *where* `0 <= i < j <
    nums.length`.

    """

    def smallest_distance_pair(self, nums: list[int], k: int) -> int:
        # Sort the array to make pair distance calculations easier
        nums.sort()

        # Helper function to count how many pairs have a distance <= mid
        def count_pairs(mid):
            count = 0
            left = 0
            # Two-pointer approach to count valid pairs
            for right in range(len(nums)):
                while nums[right] - nums[left] > mid:
                    left += 1
                count += right - left
            return count

        # Binary search for the smallest distance
        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    smallestDistancePair = smallest_distance_pair
