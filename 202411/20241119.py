# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


class Solution:
    """2461. Maximum Sum of Distinct Subarrays With Length K

    You are given an integer array `nums` and an integer `k`. Find the maximum subarray
    sum of all the subarrays of `nums` that meet the following conditions:

    * The length of the subarray is `k`, and

    * All the elements of the subarray are **distinct**.

    Return *the maximum subarray sum of all the subarrays that meet the conditions**.*
    If no subarray meets the conditions, return `0`.

    *A **subarray** is a contiguous non\\-empty sequence of elements within an array.*

    """

    def maximum_subarray_sum(self, numbers: list[int], subarray_length: int) -> int:
        # Initialize pointers for sliding window and variables for sum calculations
        left_pointer, maximum_sum, prefix_sum = 0, 0, 0
        # Use a Counter to keep track of the count of each number in the current window
        count_of_numbers = Counter()

        for right_pointer, current_number in enumerate(numbers):
            # Add the current number to the prefix sum
            prefix_sum += current_number

            # If the window size exceeds subarray_length, adjust the window
            if right_pointer - left_pointer >= subarray_length:
                count_of_numbers[numbers[left_pointer]] -= 1
                if count_of_numbers[numbers[left_pointer]] == 0:
                    del count_of_numbers[numbers[left_pointer]]
                prefix_sum -= numbers[left_pointer]
                left_pointer += 1

            # Add the current number to our count
            count_of_numbers[current_number] += 1

            # Check if we have found a valid window of distinct elements
            if len(count_of_numbers) == subarray_length:
                maximum_sum = max(prefix_sum, maximum_sum)

        # Return the maximum sum found
        return maximum_sum

    maximumSubarraySum = maximum_subarray_sum
