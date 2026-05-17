# https://leetcode.com/problems/decode-ways/


class Solution:
    """91. Decode Ways

    A message containing letters from `A-Z` can be **encoded** into numbers using the
    following mapping:

    ```

    'A' -> "1"

    'B' -> "2"

    ...

    'Z' -> "26"

    ```

    To **decode** an encoded message, all the digits must be grouped then mapped back
    into letters using the reverse of the mapping above (there may be multiple ways).
    For example, `"11106"` can be mapped into:

    * `"AAJF"` with the grouping `(1 1 10 6)`

    * `"KJF"` with the grouping `(11 10 6)`

    Note that the grouping `(1 11 06)` is invalid because `"06"` cannot be mapped into
    `'F'` since `"6"` is different from `"06"`.

    Given a string `s` containing only digits, return *the **number** of ways to
    **decode** it*.

    The test cases are generated so that the answer fits in a **32-bit** integer.
    """

    def num_decodings(self, s: str) -> int:
        # Check for empty string or leading zero, which indicates an invalid encoding.
        if not s or s[0] == "0":
            return 0

        n = len(s)
        # Initialize variables to store the previous two results in the dynamic
        # programming approach.
        prev, curr = 1, 1

        for i in range(2, n + 1):
            # Extract the current one-digit and two-digit numbers.
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2 : i])

            # Temporary variable to store the current result.
            temp = 0

            # Check if the one-digit number is valid (1-9).
            if 1 <= one_digit <= 9:
                temp += curr

            # Check if the two-digit number is valid (10-26).
            if 10 <= two_digits <= 26:
                temp += prev

            # Update the previous two results for the next iteration.
            prev, curr = curr, temp

        # When exiting the loop, curr is the number of ways to decode.
        return curr

    numDecodings = num_decodings
