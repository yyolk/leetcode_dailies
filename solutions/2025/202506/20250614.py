# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/


class Solution:
    """2566. Maximum Difference by Remapping a Digit

    You are given an integer `num`. You know that Bob will sneakily **remap** one of the
    `10` possible digits (`0` to `9`) to another digit.

    Return *the difference between the maximum and minimum values Bob can make by
    remapping **exactly** **one** digit in* `num`.

    **Notes:**

    * When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of
    `d1` in `num` with `d2`.

    * Bob can remap a digit to itself, in which case `num` does not change.

    * Bob can remap different digits for obtaining minimum and maximum values
    respectively.

    * The resulting number after remapping can contain leading zeroes."""

    def min_max_difference(self, num: int) -> int:
        s = str(num)

        # Find maximum value
        for i in range(len(s)):
            if s[i] != "9":
                d = s[i]
                max_s = s.replace(d, "9")
                break
        else:
            max_s = s  # All digits are "9", so maximum is the original number
        max_num = int(max_s)

        # Find minimum value
        for i in range(len(s)):
            if s[i] != "0":
                d = s[i]
                min_s = s.replace(d, "0")
                break
        else:
            min_s = s  # All digits are "0", so minimum is 0
        min_num = int(min_s)

        return max_num - min_num

    minMaxDifference = min_max_difference
