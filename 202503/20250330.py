# https://leetcode.com/problems/partition-labels/


class Solution:
    """763. Partition Labels

    You are given a string `s`. We want to partition the string into as many parts as
    possible so that each letter appears in at most one part. For example, the string
    `"ababcc"` can be partitioned into `["abab", "cc"]`, but partitions such as `["aba",
    "bcc"]` or `["ab", "ab", "cc"]` are invalid.

    Note that the partition is done so that after concatenating all the parts in order,
    the resultant string should be `s`.

    Return *a list of integers representing the size of these parts*."""

    def partition_labels(self, s: str) -> list[int]:
        # Step 1: Create a dictionary mapping each character to its last occurrence index
        last = {c: i for i, c in enumerate(s)}
        
        # Step 2: Initialize variables for partition boundaries and result list
        result = []
        start = 0
        end = 0
        
        # Step 3: Iterate through the string to determine partitions
        for i in range(len(s)):
            # Update the end to the farthest last occurrence of any character seen so far
            end = max(end, last[s[i]])
            # If current index equals the end, we've reached the end of a partition
            if i == end:
                # Append the length of the current partition to the result
                result.append(i - start + 1)
                # Move start to the beginning of the next partition
                start = i + 1
        
        return result

    partitionLabels = partition_labels
