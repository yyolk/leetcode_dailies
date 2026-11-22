# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/


class Solution:
    """2124. Check if All A's Appears Before All B's

    Given a string s consisting of only the characters 'a' and 'b', return
    true if every 'a' appears before every 'b' in the string. Otherwise,
    return false.

    Constraints:

    * 1 <= s.length <= 100
    * s[i] is either 'a' or 'b'.
    """

    def check_string(self, s: str) -> bool:
        # All a's precede all b's exactly when the substring "ba" is absent.
        return "ba" not in s

    checkString = check_string
