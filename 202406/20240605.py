# https://leetcode.com/problems/find-common-characters/
from collections import Counter


class Solution:
    """1002. Find Common Characters

    Given a string array `words`, return *an array of all characters that show up in all
    strings within the* `words` *(including duplicates)*. You may return the answer in
    **any order**.

    """

    def common_chars(self, words: list[str]) -> list[str]:
        # Initialize the counter with the first word of the stack
        common_count = Counter(words.pop())
        
        # Intersect the counter with all the words that are left
        for word in words:
            word_count = Counter(word)
            for char in common_count:
                if char in word_count:
                    common_count[char] = min(common_count[char], word_count[char])
                else:
                    common_count[char] = 0
        
        # Create the result list based on the common_count
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

    commonChars = common_chars
