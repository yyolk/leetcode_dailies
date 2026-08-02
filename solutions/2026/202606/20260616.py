# https://leetcode.com/problems/process-string-with-special-operations-i/


class Solution:
    """3612. Process String with Special Operations I

    You are given a string s consisting of lowercase English letters and the
    special characters: *, #, and %. Build a new string result by processing s
    according to the following rules from left to right:
    * If the letter is a lowercase English letter append it to result.
    * A '*' removes the last character from result, if it exists.
    * A '#' duplicates the current result and appends it to itself.
    * A '%' reverses the current result.
    Return the final string result after processing all characters in s.
    Constraints:
    * 1 <= s.length <= 20
    * s consists of only lowercase English letters and special characters *, #,
    and %.
    """

    def process_str(self, s: str) -> str:
        # list for O(1) append/pop/reverse/extend, optimal for n<=20
        result = []
        for char in s:
            if char.islower():
                # append lowercase English letter
                result.append(char)
            elif char == "*":
                # remove last character if result not empty
                if result:
                    result.pop()
            elif char == "#":
                # duplicate current: *=2 appends exact copy in place
                result *= 2
            elif char == "%":
                # reverse current result in-place
                result.reverse()
        # join for final string return
        return "".join(result)

    processStr = process_str
