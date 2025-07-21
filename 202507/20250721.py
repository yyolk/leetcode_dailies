# https://leetcode.com/problems/delete-characters-to-make-fancy-string/


class Solution:
    """1957. Delete Characters to Make Fancy String

    A **fancy string** is a string where no **three** **consecutive** characters are
    equal.

    Given a string `s`, delete the **minimum** possible number of characters from `s` to
    make it **fancy**.

    Return *the final string after the deletion*. It can be shown that the answer will
    always be **unique**."""

    def make_fancy_string(self, s: str) -> str:
        # If string length is less than 3, no three consecutive chars possible
        if len(s) < 3:
            return s
            
        # Convert string to list for easier manipulation
        result = []
        # Keep track of count of current character
        count = 1
        # Add first character
        result.append(s[0])
        
        # Iterate through string starting from second character
        for i in range(1, len(s)):
            # If current char same as last char in result
            if s[i] == result[-1]:
                count += 1
                # Only add if we have less than 2 consecutive same chars
                if count < 3:
                    result.append(s[i])
            else:
                # Reset count for new character
                count = 1
                result.append(s[i])
                
        return "".join(result)

    makeFancyString = make_fancy_string
