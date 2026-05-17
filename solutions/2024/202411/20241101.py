# https://leetcode.com/problems/delete-characters-to-make-fancy-string/


class Solution:
    """1957. Delete Characters to Make Fancy String

    A **fancy string** is a string where no **three** **consecutive** characters are
    equal.

    Given a string `s`, delete the **minimum** possible number of characters from `s` to
    make it **fancy**.

    Return *the final string after the deletion*. It can be shown that the answer will
    always be **unique**.

    """

    def make_fancy_string(self, s: str) -> str:
        if len(s) <= 2:  # If the string length is 2 or less, it's already fancy
            return s

        # Start with the first two characters
        result = [s[0], s[1]]

        for i in range(2, len(s)):
            # Add character if it's not the same as the last two characters in the result
            if not (len(result) >= 2 and s[i] == result[-1] == result[-2]):
                result.append(s[i])

        return "".join(result)

    makeFancyString = make_fancy_string
