# https://leetcode.com/problems/process-string-with-special-operations-ii/


class Solution:
    """3614. Process String with Special Operations II

    You are given a string s consisting of lowercase English letters and the special
    characters: '*', '#', and '%'. You are also given an integer k. Build a new string
    result by processing s according to the following rules from left to right:
    - If the letter is a lowercase English letter append it to result.
    - A '*' removes the last character from result, if it exists.
    - A '#' duplicates the current result and appends it to itself.
    - A '%' reverses the current result.
    Return the kth character of the final string result. If k is out of the bounds of
    result, return '.'.
    """

    def process_str(self, s: str, k: int) -> str:
        # Forward pass: record length after each operation (handles up to 1e15)
        n = len(s)
        lengths = [0] * (n + 1)
        for i in range(n):
            prev = lengths[i]
            c = s[i]
            if c.islower():
                lengths[i + 1] = prev + 1
            elif c == "*":
                lengths[i + 1] = max(0, prev - 1)
            elif c == "#":
                lengths[i + 1] = prev * 2
            else:  # "%"
                lengths[i + 1] = prev
        final_len = lengths[n]
        if k >= final_len:
            return "."
        # Backward trace: map k-th position (0-based) through inverse ops
        # use 1-based internal pos for consistent undo math
        pos = k + 1
        for j in range(n - 1, -1, -1):
            op = s[j]
            len_before = lengths[j]
            len_after = lengths[j + 1]
            if op.islower():
                if pos == len_after:
                    return op
                # else: pos unchanged (from previous)
            elif op == "*":
                # positions map 1:1 to before
                pass
            elif op == "#":
                half = len_before
                if pos > half:
                    pos -= half
                # else first copy: pos unchanged
            elif op == "%":
                # reverse mapping
                pos = len_before - pos + 1
        return "."

    processStr = process_str
