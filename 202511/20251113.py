# https://leetcode.com/problems/maximum-number-of-operations-to-move-ones-to-the-end/


class Solution:
    """
    3228. Maximum Number of Operations to Move Ones to the End

    You are given a binary string s.

    You can perform the following operation on the string any number of times:

    Choose any index i from the string where i + 1 < s.length such that
    s[i] == '1' and s[i + 1] == '0'.

    Move the character s[i] to the right until it reaches the end of the
    string or another '1'. For example, for s = "010010", if we choose i = 1,
    the resulting string will be s = "000110".

    Return the maximum number of operations that you can perform.
    """
    def max_operations(self, s: str) -> int:
        # Extract sizes of consecutive '1' groups
        groups = []
        i = 0
        n = len(s)
        while i < n:
            if s[i] == '1':
                count = 0
                while i < n and s[i] == '1':
                    count += 1
                    i += 1
                groups.append(count)
            else:
                i += 1
        m = len(groups)
        if m == 0:
            return 0
        # Determine if there are trailing '0's after the last '1' group
        trailing = 1 if s and s[-1] == '0' else 0
        # Calculate the maximum operations
        ans = 0
        for idx in range(m):
            # Moves for each '1' in this group: separators to the right plus trailing
            moves = (m - 1 - idx) + trailing
            ans += groups[idx] * moves
        return ans

    maxOperations = max_operations