# https://leetcode.com/problems/longest-happy-string/
from collections import Counter


class Solution:
    """1405. Longest Happy String

    A string `s` is called **happy** if it satisfies the following conditions:

    * `s` only contains the letters `"a"`, `"b"`, and `"c"`.

    * `s` does not contain any of `"aaa"`, `"bbb"`, or `"ccc"` as a substring.

    * `s` contains **at most** `a` occurrences of the letter `"a"`.

    * `s` contains **at most** `b` occurrences of the letter `"b"`.

    * `s` contains **at most** `c` occurrences of the letter `"c"`.

    Given three integers `a`, `b`, and `c`, return *the **longest possible happy**
    string*. If there are multiple longest happy strings, return *any of them*. If there
    is no such string, return *the empty string* `""`.

    A **substring** is a contiguous sequence of characters within a string.

    """

    def longest_diverse_string(self, a: int, b: int, c: int) -> str:
        """
        Generate the longest happy string given the count of "a", "b", and "c".

        :param a: Maximum number of "a"s allowed
        :param b: Maximum number of "b"s allowed
        :param c: Maximum number of "c"s allowed
        :return: The longest happy string possible with given constraints
        """
        # Use a list to build our string for efficiency in prepending/appending
        result = []
        # Counter to keep track of remaining letters
        count = Counter({"a": a, "b": b, "c": c})

        while True:
            # Sort characters by count in descending order
            for char, _ in count.most_common():
                # If the last two characters are the same as the current char, skip to next
                if len(result) >= 2 and result[-1] == result[-2] == char:
                    continue

                # If we can add this char
                if count[char] > 0:
                    result.append(char)
                    count[char] -= 1
                    break
            else:
                # If no character can be added, break out of loop
                break

            # Optimization: if we've used up the two most common characters, we're done
            if count.most_common(2)[0][1] == 0 and count.most_common(2)[1][1] == 0:
                break

        return "".join(result)

    longestDiverseString = longest_diverse_string
