# https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/


class Solution:
    """3541. Find Most Frequent Vowel and Consonant

    You are given a string `s` consisting of lowercase English letters (`'a'` to `'z'`).

    Your task is to:

    * Find the vowel (one of `'a'`, `'e'`, `'i'`, `'o'`, or `'u'`) with the **maximum**
    frequency.

    * Find the consonant (all other letters excluding vowels) with the **maximum**
    frequency.

    Return the sum of the two frequencies.

    **Note**: If multiple vowels or consonants have the same maximum frequency, you may
    choose any one of them. If there are no vowels or no consonants in the string,
    consider their frequency as 0.

    The **frequency** of a letter `x` is the number of times it occurs in the string."""

    def max_freq_sum(self, s: str) -> int:
        # Initialize frequency dictionary
        freq = {}
        for char in s:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        # Define vowels set for quick lookup
        vowels = set('aeiou')
        
        # Initialize max frequencies to 0
        max_vowel = 0
        max_consonant = 0
        
        # Find max frequency among vowels
        for v in vowels:
            if v in freq:
                max_vowel = max(max_vowel, freq[v])
        
        # Find max frequency among consonants
        for char in freq:
            if char not in vowels:
                max_consonant = max(max_consonant, freq[char])
        
        # Return sum of max frequencies
        return max_vowel + max_consonant

    maxFreqSum = max_freq_sum
