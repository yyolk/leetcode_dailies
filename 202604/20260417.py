# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs

class Solution:
    """3761. Minimum Absolute Distance Between Mirror Pairs
    
    You are given an integer array nums. A mirror pair is a pair of indices (i, j)
    such that 0 <= i < j < nums.length, and reverse(nums[i]) == nums[j], where
    reverse(x) denotes the integer formed by reversing the digits of x. Leading
    zeros are omitted after reversing, for example reverse(120) = 21. Return the
    minimum absolute distance between the indices of any mirror pair. The absolute
    distance between indices i and j is abs(i - j). If no mirror pair exists,
    return -1.
    """
    def min_mirror_pair_distance(self, nums: list[int]) -> int:
        # map: reversed_value -> most recent index i where reverse(nums[i]) equals it
        last_i = {}
        ans = -1
        for j, num in enumerate(nums):
            # query before update: check if nums[j] was produced by any prior reverse
            if num in last_i:
                dist = j - last_i[num]
                if ans == -1 or dist < ans:
                    ans = dist
            # current j now becomes a potential i for future j's using its reverse
            rev = int(str(num)[::-1])
            last_i[rev] = j
        return ans

    minMirrorPairDistance = min_mirror_pair_distance