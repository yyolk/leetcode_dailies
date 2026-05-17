# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/
from collections import Counter


class Solution:
    """3016. Minimum Number of Pushes to Type Word II

    You are given a string `word` containing lowercase English letters.

    Telephone keypads have keys mapped with **distinct** collections of lowercase
    English letters, which can be used to form words by pushing them. For example, the
    key `2` is mapped with `["a","b","c"]`, we need to push the key one time to type
    `"a"`, two times to type `"b"`, and three times to type `"c"` *.*

    It is allowed to remap the keys numbered `2` to `9` to **distinct** collections of
    letters. The keys can be remapped to **any** amount of letters, but each letter
    **must** be mapped to **exactly** one key. You need to find the **minimum** number
    of times the keys will be pushed to type the string `word`.

    Return *the **minimum** number of pushes needed to type* `word` *after remapping the
    keys*.

    An example mapping of letters to keys on a telephone keypad is given below. Note
    that `1`, `*`, `#`, and `0` do **not** map to any letters.

    ![](https://assets.leetcode.com/uploads/2023/12/26/keypaddesc.png)

    """

    def minimum_pushes(self, word: str) -> int:
        # Count the frequency of each character in the word
        char_freq = Counter(word)

        # Sort characters by frequency in descending order
        sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)

        total_pushes = 0
        for i, (char, freq) in enumerate(sorted_chars):
            # Calculate the number of pushes needed for this character
            # The first 8 characters need 1 push, the next 8 need 2 pushes, and so on
            pushes = (i // 8) + 1
            total_pushes += pushes * freq

        return total_pushes

    minimumPushes = minimum_pushes
