# https://leetcode.com/problems/construct-k-palindrome-strings/
from collections import Counter


class Solution:
    """1400. Construct K Palindrome Strings

    Given a string `s` and an integer `k`, return `true` *if you can use all the
    characters in* `s` *to construct* `k` *palindrome strings or* `false` *otherwise*.
    """

    def can_construct(self, s: str, k: int) -> bool:
        # Count the frequency of each character in s
        char_count = Counter(s)
        
        # A palindrome can have at most one character with odd count
        odd_counts = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # Check if we can construct k palindromes:
        # 1. We can have at most k characters with odd counts since each palindrome can 
        #    use up to one odd-count character.
        # 2. The number of palindromes (k) cannot exceed the number of characters.
        
        return odd_counts <= k <= len(s)

    canConstruct = can_construct
