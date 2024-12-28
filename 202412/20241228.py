# https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/


class Solution:
    """689. Maximum Sum of 3 Non-Overlapping Subarrays

    Given an integer array `nums` and an integer `k`, find three non-overlapping
    subarrays of length `k` with maximum sum and return them.

    Return the result as a list of indices representing the starting position of each
    interval (**0-indexed**). If there are multiple answers, return the
    lexicographically smallest one."""

    def max_sum_of_three_subarrays(self, nums: list[int], k: int) -> list[int]:
        # Initialize variables to keep track of the best non-overlapping sequences
        best_sequence= 0  # Starting index of the best single sequence
        best_two_sequence= [0, k]  # Starting indices of the best two sequences
        best_three_sequence= [0, k, k*2]  # Starting indices of the best three sequences

        # Calculate initial sums for the first three windows
        sequence_sum = sum(nums[0:k])  # Sum of the first window
        sequence_two_sum = sum(nums[k:k*2])  # Sum of the second window
        sequence_three_sum = sum(nums[k*2:k*3])  # Sum of the third window

        # Variables to store the sums of the best sequences found so far
        best_sequence_sum = sequence_sum  # Best sum for a single sequence
        best_two_sum = sequence_sum + sequence_two_sum  # Best sum for two sequences
        best_three_sum = sequence_sum + sequence_two_sum + sequence_three_sum  # Best sum for three sequences

        # Current indices for each window's starting position
        sequence_index = 1
        two_sequence_index = k + 1
        three_sequence_index = k*2 + 1
        
        while three_sequence_index <= len(nums) - k:
            # Slide each window by one position, updating their sums
            # Remove the first element of the previous window and add the last element of the new window
            sequence_sum = sequence_sum - nums[sequence_index - 1] + nums[sequence_index + k - 1]
            sequence_two_sum = sequence_two_sum - nums[two_sequence_index - 1] + nums[two_sequence_index + k - 1]
            sequence_three_sum = sequence_three_sum - nums[three_sequence_index - 1] + nums[three_sequence_index + k - 1]
            
            # Check if the current single sequence is better than the best found
            if sequence_sum > best_sequence_sum:
                best_sequence= sequence_index
                best_sequence_sum = sequence_sum

            # Check if the combination of the best single sequence and current second sequence is better
            if sequence_two_sum + best_sequence_sum > best_two_sum:
                best_two_sequence= [best_sequence, two_sequence_index]
                best_two_sum = sequence_two_sum + best_sequence_sum

            # Check if adding the current third sequence to the best two sequences improves the total
            if sequence_three_sum + best_two_sum > best_three_sum:
                best_three_sequence= best_two_sequence+ [three_sequence_index]
                best_three_sum = sequence_three_sum + best_two_sum

            # Move to the next position for all windows
            sequence_index += 1
            two_sequence_index += 1
            three_sequence_index += 1

        return best_three_sequence

    maxSumOfThreeSubarrays = max_sum_of_three_subarrays
