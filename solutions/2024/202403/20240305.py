# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/


class Solution:
    """1750. Minimum Length of String After Deleting Similar Ends

    Given a string `s` consisting only of characters `'a'`, `'b'`, and `'c'`. You are
    asked to apply the following algorithm on the string any number of times:

    1. Pick a **non-empty** prefix from the string `s` where all the characters in the
    prefix are equal.

    2. Pick a **non-empty** suffix from the string `s` where all the characters in this
    suffix are equal.

    3. The prefix and the suffix should not intersect at any index.

    4. The characters from the prefix and suffix must be the same.

    5. Delete both the prefix and the suffix.

    Return *the **minimum length** of* `s` *after performing the above operation any
    number of times (possibly zero times)*.

    """

    def minimum_length(self, s: str) -> int:
        # Initialize pointers for the start and end of the string
        start, end = 0, len(s) - 1

        # Continue while there are characters in the string and they are equal
        while start < end and s[start] == s[end]:
            # Move the start pointer to the right
            while start < end and s[start] == s[start + 1]:
                start += 1
            # Move the end pointer to the left
            while start < end and s[end] == s[end - 1]:
                end -= 1

            # Move both pointers inward to find the next potential prefix and suffix
            start += 1
            end -= 1

        # Return the remaining length after applying the algorithm
        return max(0, end - start + 1)

    minimumLength = minimum_length
