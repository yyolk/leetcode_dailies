# https://leetcode.com/problems/string-compression-iii/


class Solution:
    """3163. String Compression III

    Given a string `word`, compress it using the following algorithm:

    * Begin with an empty string `comp`. While `word` is **not** empty, use the
    following operation:

            + Remove a maximum length prefix of `word` made of a *single character* `c`
    repeating **at most** 9 times.

            + Append the length of the prefix followed by `c` to `comp`.

    Return the string `comp`.

    """

    def compressed_string(self, word: str) -> str:
        comp = []
        i = 0
        while i < len(word):
            # Start with the current character
            c = word[i]
            # Count consecutive occurrences of the character, up to 9
            count = 0
            while i < len(word) and word[i] == c and count < 9:
                count += 1
                i += 1

            # Append the count followed by the character to comp
            comp.append(str(count) + c)

        # Join the list into a single string for return
        return "".join(comp)

    compressedString = compressed_string
