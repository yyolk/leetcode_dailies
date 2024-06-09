# https://leetcode.com/problems/subarray-sums-divisible-by-k/


class Solution:
    """974. Subarray Sums Divisible by K

    Given an integer array `nums` and an integer `k`, return *the number of non-empty
    **subarrays** that have a sum divisible by* `k`.

    A **subarray** is a **contiguous** part of an array.

    """

    def subarrays_div_by_k(self, nums: list[int], k: int) -> int:
        # Dictionary to store the count of remainders
        remainder_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            # Add current number to the cumulative sum
            current_sum += num
            # Calculate remainder of the current sum divided by k
            remainder = current_sum % k
            # Adjust remainder to be positive
            if remainder < 0:
                remainder += k

            # If remainder is already in the dictionary, it means there are
            # some subarrays which summed up to a multiple of k
            if remainder in remainder_count:
                count += remainder_count[remainder]

            # Update the count of this remainder in the dictionary
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count

    subarraysDivByK = subarrays_div_by_k