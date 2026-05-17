# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/


class Solution:
    """1593. Split a String Into the Max Number of Unique Substrings

    Given a string `s`, return *the maximum number of unique substrings that the given
    string can be split into*.

    You can split string `s` into any list of **non\\-empty substrings**, where the
    concatenation of the substrings forms the original string. However, you must split
    the substrings such that all of them are **unique**.

    A **substring** is a contiguous sequence of characters within a string.

    """

    def max_unique_split(self, s: str) -> int:
        def backtrack(index: int, seen: set) -> int:
            # If we've reached the end of the string,
            # we've successfully split the string into unique substrings
            if index == len(s):
                return len(seen)

            max_splits = 0

            # Try all possible splits from the current index
            for i in range(index, len(s)):
                substring = s[index : i + 1]
                if substring not in seen:
                    # Add this substring to our set of seen substrings
                    seen.add(substring)
                    # Recursively try to split the rest of the string
                    current_splits = backtrack(i + 1, seen)
                    # Update max_splits if we found a better split
                    max_splits = max(max_splits, current_splits)
                    # Backtrack by removing the substring for other possibilities
                    seen.remove(substring)

            return max_splits

        # Start the backtracking from index 0 with an empty set of seen substrings
        return backtrack(0, set())

    maxUniqueSplit = max_unique_split
