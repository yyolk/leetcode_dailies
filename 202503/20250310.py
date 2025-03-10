# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/


class Solution:
    """3306. Count of Substrings Containing Every Vowel and K Consonants II

    You are given a string `word` and a **non-negative** integer `k`.

    Return the total number of substrings of `word` that contain every vowel (`"a"`,
    `"e"`, `"i"`, `"o"`, and `"u"`) **at least** once and **exactly** `k` consonants."""

    def count_of_substrings(self, word: str, k: int) -> int:
        # Define the set of vowels for quick lookup
        vowels = set("aeiou")
        # Get the length of the word
        n = len(word)
        # Initialize the result to store the total count of valid substrings
        result = 0
        
        # Precompute next_consonant array: for each index i, store the next index where a consonant occurs
        # If no consonant follows, store n (end of string)
        next_consonant = [n] * n  # Initialize all positions to n
        next_cons_index = n  # Start with the end of the string as the next consonant position
        for i in range(n - 1, -1, -1):  # Iterate backwards through the string
            next_consonant[i] = next_cons_index  # Set the next consonant index for position i
            if word[i] not in vowels:  # If current character is a consonant
                next_cons_index = i  # Update the next consonant position to current index

        # Initialize data structures for the sliding window
        vowel_count = {}  # Dictionary to count occurrences of each vowel in the window
        cons_count = 0    # Counter for consonants in the window
        left = 0          # Left pointer of the sliding window

        # Iterate over the string with the right pointer
        for right in range(n):
            ch = word[right]  # Current character at right pointer
            # Update counts based on whether the character is a vowel or consonant
            if ch in vowels:
                vowel_count[ch] = vowel_count.get(ch, 0) + 1  # Increment vowel count
            else:
                cons_count += 1  # Increment consonant count

            # Shrink the window from the left if there are too many consonants
            while cons_count > k and left <= right:
                left_ch = word[left]  # Character at the left pointer
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1  # Decrease vowel count
                    if vowel_count[left_ch] == 0:  # If count becomes zero
                        del vowel_count[left_ch]  # Remove the vowel from the dictionary
                else:
                    cons_count -= 1  # Decrease consonant count
                left += 1  # Move left pointer to shrink the window

            # Check for valid windows with exactly k consonants and all five vowels
            while left <= right and cons_count == k and len(vowel_count) == 5:
                # Count all substrings by extending the current window to the next consonant
                # next_consonant[right] - right gives the number of vowels that can be added
                # without adding more consonants
                result += next_consonant[right] - right

                # Shrink the window from the left to avoid double-counting and find new valid windows
                left_ch = word[left]
                if left_ch in vowels:
                    vowel_count[left_ch] -= 1  # Decrease vowel count
                    if vowel_count[left_ch] == 0:  # If count becomes zero
                        del vowel_count[left_ch]  # Remove the vowel
                else:
                    cons_count -= 1  # Decrease consonant count
                left += 1  # Move left pointer forward

        # Return the total number of valid substrings
        return result

    countOfSubstrings = count_of_substrings
