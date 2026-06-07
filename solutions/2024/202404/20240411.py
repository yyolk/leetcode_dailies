# https://leetcode.com/problems/remove-k-digits/


class Solution:
    """402. Remove K Digits

    Given string num representing a non-negative integer `num`, and an integer `k`,
    return *the smallest possible integer after removing* `k` *digits from* `num`.

    """

    def remove_kdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0

        for digit in num:
            while stack and removed < k and stack[-1] > digit:
                stack.pop()
                removed += 1
            stack.append(digit)

        # Handle the case where all digits are the same and k is not reached
        while removed < k:
            stack.pop()
            removed += 1

        # Remove leading zeros
        return "".join(stack).lstrip("0") or "0"

    removeKdigits = remove_kdigits
