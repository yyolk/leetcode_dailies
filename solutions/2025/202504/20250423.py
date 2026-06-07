# https://leetcode.com/problems/count-largest-group/


class Solution:
    """1399. Count Largest Group

    You are given an integer `n`.

    Each number from `1` to `n` is grouped according to the sum of its digits.

    Return *the number of groups that have the largest size*."""

    def count_largest_group(self, n: int) -> int:
        # Initialize a list to count numbers for each digit sum (1 to 36)
        counts = [0] * 37  # Index 0 is unused; 1 to 36 correspond to possible sums

        # Calculate digit sum for each number from 1 to n and update counts
        for i in range(1, n + 1):
            s = 0
            temp = i
            # Compute sum of digits
            while temp > 0:
                s += temp % 10  # Add the last digit
                temp = temp // 10  # Remove the last digit
            counts[s] += 1  # Increment the count for this digit sum

        # Find the size of the largest group
        max_size = max(counts[1:])  # Ignore index 0

        # Count how many groups have the largest size
        return counts.count(max_size)

    countLargestGroup = count_largest_group
