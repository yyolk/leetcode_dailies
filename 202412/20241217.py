# https://leetcode.com/problems/construct-string-with-repeat-limit/
from collections import Counter


class Solution:
    """2182. Construct String With Repeat Limit

    You are given a string `s` and an integer `repeat_limit`. Construct a new string
    `repeat_limitedString` using the characters of `s` such that no letter appears
    **more than** `repeat_limit` times **in a row**. You do **not** have to use all
    characters from `s`.

    Return *the **lexicographically largest*** `repeat_limitedString` *possible*.

    A string `a` is **lexicographically larger** than a string `b` if in the first
    position where `a` and `b` differ, string `a` has a letter that appears later in the
    alphabet than the corresponding letter in `b`. If the first `min(a.length,
    b.length)` characters do not differ, then the longer string is the lexicographically
    larger one."""

    def repeat_limited_string(self, s: str, repeat_limit: int) -> str:
        char_count = Counter(s)
        
        result = []
        prev_char = None
        prev_count = 0
        
        while char_count:
            # Always try to append the highest possible character
            for char in sorted(char_count.keys(), reverse=True):
                if char != prev_char:
                    # If we've changed characters, reset the count
                    result.append(char)
                    char_count[char] -= 1
                    if char_count[char] == 0:
                        del char_count[char]
                    prev_char = char
                    prev_count = 1
                    break
                elif prev_count < repeat_limit:
                    # We can add one more of the same character if under the limit
                    result.append(char)
                    char_count[char] -= 1
                    if char_count[char] == 0:
                        del char_count[char]
                    prev_count += 1
                    break
            else:
                # If we couldn't add any character, we're done
                break
        
        return "".join(result)

    repeatLimitedString = repeat_limited_string
