# https://leetcode.com/problems/construct-the-lexicographically-largest-valid-sequence/


class Solution:
    """1718. Construct the Lexicographically Largest Valid Sequence

    Given an integer `n`, find a sequence that satisfies all of the following:

    * The integer `1` occurs once in the sequence.

    * Each integer between `2` and `n` occurs twice in the sequence.

    * For every integer `i` between `2` and `n`, the **distance** between the two
    occurrences of `i` is exactly `i`.

    The **distance** between two numbers on the sequence, `a[i]` and `a[j]`, is the
    absolute difference of their indices, `|j - i|`.

    Return *the **lexicographically largest** sequence**. It is guaranteed that under
    the given constraints, there is always a solution.*

    A sequence `a` is lexicographically larger than a sequence `b` (of the same length)
    if in the first position where `a` and `b` differ, sequence `a` has a number greater
    than the corresponding number in `b`. For example, `[0,1,9,0]` is lexicographically
    larger than `[0,1,5,6]` because the first position they differ is at the third
    number, and `9` is greater than `5`."""

    def construct_distanced_sequence(self, n: int) -> list[int]:
        # The length of the sequence
        length = 2 * n - 1
        # Initialize the sequence with zeros
        sequence = [0] * length
        # Track which numbers have been used
        used = [False] * (n + 1)

        def backtrack(index):
            if index == length:
                # We have successfully filled the sequence
                return True

            if sequence[index] != 0:
                # Move to the next position
                return backtrack(index + 1)

            # Try placing the largest possible number first to ensure lexicographical order
            for num in range(n, 0, -1):
                if used[num]:
                    # Skip if the number is already used
                    continue

                if num == 1:
                    sequence[index] = 1
                    used[1] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    used[1] = False
                else:
                    if index + num >= length or sequence[index + num] != 0:
                        # Cannot place the second occurrence
                        continue

                    sequence[index] = num
                    sequence[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    sequence[index] = 0
                    sequence[index + num] = 0
                    used[num] = False

            # No valid placement found
            return False

        backtrack(0)
        return sequence

    constructDistancedSequence = construct_distanced_sequence
