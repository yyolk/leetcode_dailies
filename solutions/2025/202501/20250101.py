# https://leetcode.com/problems/maximum-score-after-splitting-a-string/


class Solution:
    """1422. Maximum Score After Splitting a String

    Given a string `s` of zeros and ones, *return the maximum score after splitting the
    string into two **non-empty** substrings* (i.e. **left** substring and **right**
    substring).

    The score after splitting a string is the number of **zeros** in the **left**
    substring plus the number of **ones** in the **right** substring.
    """

    def max_score(self, s: str) -> int:
        max_score = 0
        zeros_count = 0
        # Count the number of ones in the whole string.
        ones_count = s.count("1")

        # Iterate through the string
        for i in range(len(s) - 1):
            if s[i] == "0":
                # Increment zeros count for left substring.
                zeros_count += 1
            else:
                # Decrement ones count for right substring.
                ones_count -= 1

            # Calculate current score for the split.
            current_score = zeros_count + ones_count

            # Update max_score if the current score is higher.
            max_score = max(max_score, current_score)

        return max_score

    maxScore = max_score
