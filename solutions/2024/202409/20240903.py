# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/


class Solution:
    """1945. Sum of Digits of String After Convert

    You are given a string `s` consisting of lowercase English letters, and an integer
    `k`.

    First, **convert** `s` into an integer by replacing each letter with its position in
    the alphabet (i.e., replace `"a"` with `1`, `"b"` with `2`, ..., `"z"` with `26`).
    Then, **transform** the integer by replacing it with the **sum of its digits**.
    Repeat the **transform** operation `k` **times** in total.

    For example, if `s = "zbax"` and `k = 2`, then the resulting integer would be `8` by
    the following operations:

    * **Convert**: `"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124`

    * **Transform \\#1**: `262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17`

    * **Transform \\#2**: `17 ➝ 1 + 7 ➝ 8`

    Return *the resulting integer after performing the operations described above*.

    """

    def get_lucky(self, s: str, k: int) -> int:
        # Convert string to number string where "a" -> "1", "b" -> "2", etc.
        num_str = "".join(str(ord(c) - ord("a") + 1) for c in s)

        # Perform k transformations
        result = num_str
        for _ in range(k):
            # Sum the digits of the current number
            digit_sum = sum(int(digit) for digit in result)
            # If we"ve done all transformations, break early
            if _ == k - 1:
                return digit_sum
            # Otherwise, prepare for next transformation
            result = str(digit_sum)

        # This line should not be reached if k > 0, but included for completeness
        return int(result)

    getLucky = get_lucky
