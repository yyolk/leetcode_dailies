# https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

class Solution:
    """3514. Number of Unique XOR Triplets II
    
    You are given an integer array `nums`.
    A **XOR triplet** is defined as the XOR of three elements `nums[i] XOR
    nums[j] XOR nums[k]` where `i <= j <= k`.
    Return the number of **unique** XOR triplet values from all possible
    triplets `(i, j, k)`.
    Constraints:
    * `1 <= nums.length <= 1500`
    * `1 <= nums[i] <= 1500`
    """
    def unique_xor_triplets(self, nums: list[int]) -> int:
        # Unique values suffice; equal indices allow replacement
        uniq = list(set(nums))
        # Boolean flags for possible XOR of any two (incl. same)
        pair = [False] * 2048
        for a in uniq:
            for b in uniq:
                pair[a ^ b] = True
        # Boolean flags for possible XOR of three = (a^b) ^ c
        tri = [False] * 2048
        for px in range(2048):
            if pair[px]:
                for c in uniq:
                    tri[px ^ c] = True
        # Number of unique possible triplet XOR values
        return sum(tri)

    uniqueXorTriplets = unique_xor_triplets
