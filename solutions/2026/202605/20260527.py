# https://leetcode.com/problems/count-the-number-of-special-characters-ii/


class Solution:
    """3121. Count the Number of Special Characters II

    You are given a string `word`. A letter `c` is called **special** if it appears
    both in lowercase and uppercase in `word`, and every lowercase occurrence of `c`
    appears before the first uppercase occurrence of `c`.
    Return the number of special letters in `word`.
    """

    def number_of_special_chars(self, word: str) -> int:
        # Track last index of each lowercase a-z
        last_lower = [-1] * 26
        # Track first index of each uppercase A-Z, init beyond string end
        first_upper = [len(word)] * 26

        for i, c in enumerate(word):
            if "a" <= c <= "z":
                idx = ord(c) - ord("a")
                last_lower[idx] = i  # update last lowercase position
            elif "A" <= c <= "Z":
                idx = ord(c) - ord("A")
                if i < first_upper[idx]:
                    first_upper[idx] = i  # update first uppercase position

        count = 0
        for i in range(26):
            # Has both cases and all lowers before first upper
            if (
                last_lower[i] != -1
                and first_upper[i] < len(word)
                and last_lower[i] < first_upper[i]
            ):
                count += 1
        return count

    numberOfSpecialChars = number_of_special_chars
