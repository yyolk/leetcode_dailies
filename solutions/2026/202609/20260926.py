# https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/


class Solution:
    """1807. Evaluate the Bracket Pairs of a String

    You are given a string `s` that contains some bracket pairs, with each pair
    containing a **non-empty** key.

    * For example, in the string `"(name)is(age)yearsold"`, there are **two**
    bracket pairs that contain the keys `"name"` and `"age"`.

    You know the values of a wide range of keys. This is represented by a 2D
    string array `knowledge` where each `knowledge[i] = [keyi, valuei]`
    indicates that key `keyi` has a value of `valuei`.

    You are tasked to evaluate **all** of the bracket pairs. When you evaluate a
    bracket pair that contains some key `keyi`, you will:

    * Replace `keyi` and the bracket pair with the key's corresponding
    `valuei`.

    * If you do not know the value of the key, you will replace `keyi` and the
    bracket pair with a question mark `"?"` (without the quotation marks).

    Each key will appear at most once in your `knowledge`. There will not be any
    nested brackets in `s`.

    Return *the resulting string after evaluating **all** of the bracket pairs.*

    Constraints:

    * `1 <= s.length <= 105`

    * `0 <= knowledge.length <= 105`

    * `knowledge[i].length == 2`

    * `1 <= keyi.length, valuei.length <= 10`

    * `s` consists of lowercase English letters and round brackets `'('` and
    `')'`.

    * Every open bracket `'('` in `s` will have a corresponding close bracket
    `')'`.

    * The key in each bracket pair of `s` will be non-empty.

    * There will not be any nested bracket pairs in `s`.

    * `keyi` and `valuei` consist of lowercase English letters.

    * Each `keyi` in `knowledge` is unique.
    """

    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        """Replace each `(key)` with its knowledge value, or `?` if unknown."""
        # O(1) lookup; keys are unique per the problem statement.
        lookup = {key: value for key, value in knowledge}
        parts: list[str] = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] != "(":
                parts.append(s[i])
                i += 1
                continue
            # Scan the non-empty key between this '(' and its matching ')'.
            j = i + 1
            while j < n and s[j] != ")":
                j += 1
            parts.append(lookup.get(s[i + 1 : j], "?"))
            i = j + 1
        return "".join(parts)
