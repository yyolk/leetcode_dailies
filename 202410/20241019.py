# https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/


class Solution:
    """1545. Find Kth Bit in Nth Binary String

    Given two positive integers `n` and `k`, the binary string `Sn` is formed as
    follows:

    * `S1 = "0"`

    * `Si = Si - 1 + "1" + reverse(invert(Si - 1))` for `i > 1`

    Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed
    string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1`
    changes to `0`).

    For example, the first four strings in the above sequence are:

    * `S1 = "0"`

    * `S2 = "011"`

    * `S3 = "0111001"`

    * `S4 = "011100110110001"`

    Return *the* `kth` *bit* *in* `Sn`. It is guaranteed that `k` is valid for the given
    `n`.

    """

    def invert(self, s: str) -> str:
        """Inverts the binary string."""
        return "".join("1" if bit == "0" else "0" for bit in s)

    def find_kth_bit(self, n: int, k: int) -> str:
        """
        Finds the kth bit in the nth binary string Sn.

        Args:
        n: The index of the binary string sequence.
        k: The position of the bit to find (1-indexed).

        Returns:
        The kth bit in Sn, "0" or "1".
        """
        # Base case
        if n == 1:
            return "0"

        # Recursive behavior:
        # The kth bit of Sn can be determined from Sn-1
        # If k is in the first half of Sn, it"s the same as in Sn-1
        # If k is in the second half, it"s the inverse of the mirrored position in Sn-1
        s = "0"  # Starting with S1

        for i in range(2, n + 1):
            # Build Si from Si-1
            s = s + "1" + self.invert(s)[::-1]

        return s[k - 1]

    findKthBit = find_kth_bit
