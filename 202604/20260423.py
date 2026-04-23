# https://leetcode.com/problems/sum-of-distances

class Solution:
    """2615. Sum of Distances
    
    You are given a 0-indexed integer array nums. There exists an array arr of
    length nums.length, where arr[i] is the sum of |i - j| over all j such that
    nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.
    Return the array arr.
    """
    def distance(self, nums: list[int]) -> list[int]:
        # group indices by value (already sorted within each group)
        groups = {}
        for i, num in enumerate(nums):
            if num not in groups:
                groups[num] = []
            groups[num].append(i)

        arr = [0] * len(nums)
        for pos in groups.values():
            m = len(pos)
            if m < 2:
                continue
            # prefix sums allow O(1) left/right distance sums per index
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + pos[i]
            for i in range(m):
                left_count = i
                left_sum = prefix[i]
                right_count = m - i - 1
                right_sum = prefix[m] - prefix[i + 1]
                # sum of absolute diffs = left diffs + right diffs
                arr[pos[i]] = (left_count * pos[i] - left_sum) + (right_sum - right_count * pos[i])
        return arr

    distance = distance