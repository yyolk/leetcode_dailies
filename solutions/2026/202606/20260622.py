# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    """1189. Maximum Number of Balloons
    
    Given a string text, you want to use the characters of text to form as many
    instances of the word "balloon" as possible. You can use each character in
    text at most once. Return the maximum number of instances that can be formed.
    Constraints:
    * 1 <= text.length <= 104
    * text consists of lower case English letters only."""
    def max_number_of_balloons(self, text: str) -> int:
        # freq array for a-z - O(1) extra space, single O(n) pass for speed
        freq = [0] * 26
        for char in text:
            freq[ord(char) - ord("a")] += 1
        # extract needed counts (balloon requires b:1 a:1 l:2 o:2 n:1)
        b = freq[ord("b") - ord("a")]
        a = freq[ord("a") - ord("a")]
        l = freq[ord("l") - ord("a")]
        o = freq[ord("o") - ord("a")]
        n = freq[ord("n") - ord("a")]
        # min after floor div for letters needing 2 copies
        return min(b, a, l // 2, o // 2, n)

    maxNumberOfBalloons = max_number_of_balloons