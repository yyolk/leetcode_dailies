# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/


class Solution:
    """1437. Check If All 1's Are at Least Length K Places Away

    Given an binary array nums and an integer k, return true if all 1's are
    at least k places away from each other, otherwise return false.
    """
    def k_length_apart(self, nums: list[int], k: int) -> bool:
        # Initialize previous 1's position to -1 (none seen yet)
        prev = -1
        # Iterate through each index in nums
        for i in range(len(nums)):
            # Check if current element is 1
            if nums[i] == 1:
                # If a previous 1 exists and distance between is less than k
                if prev != -1 and i - prev - 1 < k:
                    return False
                # Update previous position to current
                prev = i
        # All 1's are sufficiently apart
        return True

    kLengthApart = k_length_apart