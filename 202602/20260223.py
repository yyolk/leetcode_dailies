# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k


class Solution:
    """1461. Check If a String Contains All Binary Codes of Size K

    Given a binary string s and an integer k, return true if every binary code of
    length k is a substring of s. Otherwise, return false.
    """
    def has_all_codes(self, s: str, k: int) -> bool:
        n: int = len(s)
        if n < k:
            # impossible to have any substring of length k
            return False
        total: int = 1 << k
        if n - k + 1 < total:
            # not enough windows to contain all unique codes
            return False
        seen: set[int] = set()
        # build integer for first window of k bits (MSB first)
        window: int = int(s[:k], 2)
        seen.add(window)
        # mask keeps exactly k lowest bits during rolling
        mask: int = (1 << k) - 1
        # slide the window from position k to end
        for i in range(k, n):
            # drop MSB, shift left, add new LSB from s[i]
            window = ((window << 1) & mask) | int(s[i])
            seen.add(window)
        return len(seen) == total

    hasAllCodes = has_all_codes