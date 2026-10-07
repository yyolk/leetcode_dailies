# https://leetcode.com/problems/remove-invalid-parentheses/


class Solution:
    """301. Remove Invalid Parentheses

    Given a string s that contains parentheses and letters, remove the
    minimum number of invalid parentheses to make the input string valid.

    Return a list of unique strings that are valid with the minimum number
    of removals. You may return the answer in any order.

    Constraints:

    * 1 <= s.length <= 25
    * s consists of lowercase English letters and parentheses '(' and ')'.
    * There will be at most 20 parentheses in s.
    """

    def remove_invalid_parentheses(self, s: str) -> list[str]:
        """Return every unique string after the fewest parenthesis removals."""
        results: list[str] = []

        def remove(
            text: str,
            start: int,
            last_removed: int,
            open_ch: str,
            close_ch: str,
        ) -> None:
            balance = 0
            for i in range(start, len(text)):
                char = text[i]
                if char == open_ch:
                    balance += 1
                elif char == close_ch:
                    balance -= 1
                if balance >= 0:
                    continue
                # Drop one unmatched close, skipping consecutive duplicates.
                for j in range(last_removed, i + 1):
                    if text[j] == close_ch and (
                        j == last_removed or text[j - 1] != close_ch
                    ):
                        remove(
                            text[:j] + text[j + 1 :],
                            i,
                            j,
                            open_ch,
                            close_ch,
                        )
                return
            reversed_text = text[::-1]
            if open_ch == "(":
                # Extra opens are unmatched closes after reversing the string.
                remove(reversed_text, 0, 0, ")", "(")
            else:
                results.append(reversed_text)

        remove(s, 0, 0, "(", ")")
        return results

    removeInvalidParentheses = remove_invalid_parentheses
