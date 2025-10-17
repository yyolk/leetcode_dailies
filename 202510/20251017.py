# https://leetcode.com/problems/maximize-the-number-of-partitions-after-operations/
from functools import cache


class Solution:
    """3003. Maximize the Number of Partitions After Operations

    You are given a string `s` and an integer `k`.

    First, you are allowed to change **at most** **one** index in `s` to another
    lowercase English letter.

    After that, do the following partitioning operation until `s` is **empty**:

    * Choose the **longest** **prefix** of `s` containing at most `k` **distinct**
    characters.

    * **Delete** the prefix from `s` and increase the number of partitions by one. The
    remaining characters (if any) in `s` maintain their initial order.

    Return an integer denoting the **maximum** number of resulting partitions after the
    operations by optimally choosing at most one index to change."""

    def max_partitions_after_operations(self, s: str, k: int) -> int:
        # Memoized recursive function
        @cache
        def dfs(index: int, current_chars: int, can_change: int) -> int:
            # Base case: end of string reached, count the current partition
            if index >= n:
                return 1

            # Bit for the current character
            char_bit = 1 << (ord(s[index]) - ord('a'))

            # Attempt to add current character to the partition
            next_chars = current_chars | char_bit

            # If adding exceeds k distinct, start a new partition
            if next_chars.bit_count() > k:
                result = dfs(index + 1, char_bit, can_change) + 1
            else:
                # Continue with the current partition
                result = dfs(index + 1, next_chars, can_change)

            # If change is still available, try changing the current character
            if can_change:
                for letter_index in range(26):
                    # Bit for the new letter
                    new_bit = 1 << letter_index
                    next_chars = current_chars | new_bit

                    # If adding the new letter exceeds k, start a new partition
                    if next_chars.bit_count() > k:
                        result = max(result, dfs(index + 1, new_bit, 0) + 1)
                    else:
                        # Continue with the current partition
                        result = max(result, dfs(index + 1, next_chars, 0))

            return result

        # Length of the string
        n = len(s)

        # Start from index 0 with empty mask and change available
        return dfs(0, 0, 1)

    maxPartitionsAfterOperations = max_partitions_after_operations
