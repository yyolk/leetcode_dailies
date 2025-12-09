# https://leetcode.com/problems/count-special-triplets


class Solution:
    """3583. Count Special Triplets

    You are given an integer array nums.

    A special triplet is defined as a triplet of indices (i, j, k) such that:

    0 <= i < j < k < n, where n = nums.length
    nums[i] == nums[j] * 2
    nums[k] == nums[j] * 2
    Return the total number of special triplets in the array.

    Since the answer may be large, return it modulo 10**9 + 7.
    """
    def special_triplets(self, nums: list[int]) -> int:
        # Early return for empty array
        if not nums:
            return 0
        
        MOD = 10**9 + 7
        # Precompute total frequency of each value in nums
        total_freq = Counter(nums)
        # Counter for frequencies to the left of current j
        freq_left = Counter()
        # Accumulate answer modulo MOD
        ans = 0
        
        for j in range(len(nums)):
            # Target value for i and k: twice nums[j]
            target = 2 * nums[j]
            # Count of target in left (i < j)
            left_count = freq_left.get(target, 0)
            # Total occurrences of target
            total = total_freq.get(target, 0)
            # Whether current nums[j] is target (only if nums[j] == 0)
            curr = 1 if nums[j] == target else 0
            # Count of target in right (k > j)
            right_count = total - left_count - curr
            # Add contribution: left * right, modulo MOD
            ans = (ans + left_count * right_count) % MOD
            # Update left frequency for next j
            freq_left[nums[j]] += 1
        
        return ans

    specialTriplets = special_triplets