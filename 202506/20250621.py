# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/


class Solution:
    """3085. Minimum Deletions to Make String K-Special

    You are given a string `word` and an integer `k`.

    We consider `word` to be **k-special** if `|freq(word[i]) - freq(word[j])| <= k` for
    all indices `i` and `j` in the string.

    Here, `freq(x)` denotes the frequency of the character `x` in `word`, and `|y|`
    denotes the absolute value of `y`.

    Return *the **minimum** number of characters you need to delete to make* `word`
    ***k-special***."""

    def minimum_deletions(self, word: str, k: int) -> int:
        # Step 1: Count the frequency of each character in the string
        freq = Counter(word)

        # Step 2: Extract the list of frequencies for characters with count > 0
        freq_list = [freq[c] for c in freq if freq[c] > 0]

        # Handle edge case: if the string is empty (though constraints ensure length >= 1)
        if not freq_list:
            return 0

        # Step 3: Determine the maximum frequency to set the range for min_t
        max_freq = max(freq_list)

        # Step 4: Initialize the maximum number of characters we can keep
        max_sum = 0

        # Step 5: Iterate over all possible minimum frequencies (min_t)
        for min_t in range(1, max_freq + 1):
            # For each min_t, calculate how many characters we can keep
            # by taking min(f, min_t + k) for frequencies >= min_t
            sum_t = sum(min(f, min_t + k) for f in freq_list if f >= min_t)
            # Update max_sum if this sum is greater
            max_sum = max(max_sum, sum_t)

        # Step 6: Calculate total length of the string
        total_length = sum(freq_list)

        # Step 7: Minimum deletions is total length minus maximum characters we can keep
        return total_length - max_sum

    minimumDeletions = minimum_deletions
