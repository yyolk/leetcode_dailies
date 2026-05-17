# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/


class Solution:
    """1432. Max Difference You Can Get From Changing an Integer

    You are given an integer `num`. You will apply the following steps to `num` **two**
    separate times:

    * Pick a digit `x (0 <= x <= 9)`.

    * Pick another digit `y (0 <= y <= 9)`. Note `y` can be equal to `x`.

    * Replace all the occurrences of `x` in the decimal representation of `num` by `y`.

    Let `a` and `b` be the two results from applying the operation to `num`
    *independently*.

    Return *the max difference* between `a` and `b`.

    Note that neither `a` nor `b` may have any leading zeros, and **must not** be 0."""

    def max_diff(self, num: int) -> int:
        # Convert number to string for digit manipulation
        s = str(num)

        # Calculate maximum possible value (a)
        # Find the leftmost digit less than 9 and replace all occurrences with 9
        for i in range(len(s)):
            if s[i] < "9":
                d = s[i]
                a_str = s.replace(d, "9")
                break
        else:
            # If all digits are 9, keep the number as is
            a_str = s
        a = int(a_str)

        # Calculate minimum possible value (b)
        d = s[0]  # First digit
        candidates = []

        # Case 1: Replace digits after the first that differ from the first digit with 0
        if len(s) > 1:
            for x in set(s[1:]):  # Unique digits after the first position
                if x > "0" and x != d:
                    b_str = s.replace(x, "0")
                    candidates.append(int(b_str))

        # Case 2: If first digit > 1, replace all occurrences with 1
        if d > "1":
            b_str = s.replace(d, "1")
            candidates.append(int(b_str))

        # If no candidates (e.g., num=111 or num=10), keep original number
        if candidates:
            b = min(candidates)
        else:
            b = num

        # Return the maximum difference
        return a - b

    maxDiff = max_diff
