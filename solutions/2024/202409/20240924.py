# https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/


class Solution:
    """3043. Find the Length of the Longest Common Prefix

    You are given two arrays with **positive** integers `arr1` and `arr2`.

    A **prefix** of a positive integer is an integer formed by one or more of its
    digits, starting from its **leftmost** digit. For example, `123` is a prefix of the
    integer `12345`, while `234` is **not**.

    A **common prefix** of two integers `a` and `b` is an integer `c`, such that `c` is
    a prefix of both `a` and `b`. For example, `5655359` and `56554` have a common
    prefix `565` while `1223` and `43456` **do not** have a common prefix.

    You need to find the length of the **longest common prefix** between all pairs of
    integers `(x, y)` such that `x` belongs to `arr1` and `y` belongs to `arr2`.

    Return *the length of the **longest** common prefix among all pairs*. *If no common
    prefix exists among them*, *return* `0`.

    """

    def longest_common_prefix(self, arr1: list[int], arr2: list[int]) -> int:
        # Dictionary to store all prefixes from arr1
        prefix_map = {}

        # Build the prefix map for arr1
        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                # Build prefix character by character
                prefix += ch
                # Add or update prefix in the map; increment count or initialize to 1
                prefix_map[prefix] = prefix_map.get(prefix, 0) + 1

        # Track the longest common prefix length
        max_length = 0

        # Check for common prefixes in arr2
        for num in arr2:
            str_num = str(num)
            prefix = ""
            for i, ch in enumerate(str_num):
                prefix += ch
                # If this prefix exists in our map, update max_length if necessary
                if prefix in prefix_map:
                    max_length = max(
                        max_length, i + 1
                    )  # i + 1 because enumerate starts at 0
                else:
                    # No need to continue with this number if no match at this length
                    break

        # Return the length of the longest common prefix found
        return max_length

    longestCommonPrefix = longest_common_prefix
