# https://leetcode.com/problems/count-number-of-nice-subarrays/


class Solution:
    """1248. Count Number of Nice Subarrays

    Given an array of integers `nums` and an integer `k`. A continuous subarray is
    called **nice** if there are `k` odd numbers on it.

    Return *the number of **nice** sub-arrays*.

    """

    def number_of_subarrays(self, nums: list[int], k: int) -> int:
        # Step 1: Transform the nums array to 1s and 0s
        nums = [1 if x % 2 != 0 else 0 for x in nums]

        # Step 2: Use prefix sum and hashmap to count nice subarrays
        count = {
            0: 1
        }  # Initialize with 0:1 to handle the subarrays starting from index 0
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in count:
                result += count[prefix_sum - k]
            if prefix_sum in count:
                count[prefix_sum] += 1
            else:
                count[prefix_sum] = 1

        return result

    numberOfSubarrays = number_of_subarrays
