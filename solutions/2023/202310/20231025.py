# https://leetcode.com/problems/k-th-symbol-in-grammar/


class Solution:
    """779. K-th Symbol in Grammar

    We build a table of `n` rows (**1-indexed**). We start by writing `0` in the `1st`
    row. Now in every subsequent row, we look at the previous row and replace each
    occurrence of `0` with `01`, and each occurrence of `1` with `10`.

    * For example, for `n = 3`, the `1st` row is `0`, the `2nd` row is `01`, and the
    `3rd` row is `0110`.

    Given two integer `n` and `k`, return the `kth` (**1-indexed**) symbol in the `nth`
    row of a table of `n` rows.
    """

    def kth_grammar(self, n: int, k: int) -> int:
        """Returns the kth symbol in the nth row of a table of n rows.

        Proposed solution using recursion.

        Args:
            n (int): Input n for rows in table.
            k (int): Query k for kth symbol in the nth row of a table of n rows.

        Returns:
            int: The kth symbol in the nth row of a table of n rows.
        """
        # Base case
        if n == 1:
            return 0

        # Calculate the length of the (n-1)th row
        length_of_prev_row = 2 ** (n - 1 - 1)

        # If k is the first half of the row, it's the same as in the (n-1)th row
        if k <= length_of_prev_row:
            return self.kth_grammar(n - 1, k)
        # If k is in the second half, it's the opposite of the (n-1)th row
        else:
            return 1 - self.kth_grammar(n - 1, k - length_of_prev_row)

    kthGrammar = kth_grammar
