# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import Counter


class Solution:
    """1647. Minimum Deletions to Make Character Frequencies Unique

    A string `s` is called **good** if there are no two different characters in `s` that
    have the same **frequency**.

    Given a string `s`, return *the **minimum** number of characters you need to delete to
    make* `s` ***good**.*

    The **frequency** of a character in a string is the number of times it appears in the
    string. For example, in the string `"aab"`, the **frequency** of `'a'` is `2`, while the
    **frequency** of `'b'` is `1`.
    """

    def minDeletions(self, s: str) -> int:
        """The minimum deletions to make character sequence input "good".

        Proposed solution, tracking the frequency of each character and dynamic programming.

        Args:
            s (str): the input string of characters (s in string.ascii_lower)

        Returns:
            int: the minimum number of characters to delete to make s good
        """
        # Count occurences of each letter with a Counter
        freqs = Counter(s)

        # Track unique frequencies and total deletions
        unique_freqs = set()
        deletions = 0

        # Iter over all freqs to fill in frequencies that are empty
        # to make this a good string
        for freq in freqs.values():
            while freq in unique_freqs:
                freq -= 1
                deletions += 1
            if freq > 0:
                unique_freqs.add(freq)

        # The number of deletions we've completed is the minimum possible
        # for a good string
        return deletions
