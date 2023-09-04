# https://leetcode.com/problems/counting-bits/


class Solution:
    """338. Counting Bits

    Given an integer `n`, return *an array* `ans` *of length* `n + 1` *such that for
    each* `i`(`0 <= i <= n`)*,* `ans[i]` *is the **number of*** `1`***'s** in the
    binary representation of* `i`.
    """

    def countBits(self, n: int) -> List[int]:
        """Count the bits

        Proposed solution uses dynamic programming in a way.
        It also uses bit shifting and binary math operator of `&`

        Args:
            n (int): The given input of integer `n`

        Returns:
            List of int: Answers of length `n + 1` where i is `0 <= i <= n`
                and `Answers[i]` is the number of `1`'s in the binary
                representation of `i`
        """
        # Initial array to store counts of 1's in binary representation
        ans = [0] * (n + 1)

        # Iterate through numbers 1 to n
        for i in range(1, n + 1):
            # Calculate the count of 1's for the current number
            # ans[i >> 1] retrieves the count from the right-shifted version
            # (i & 1) checks if the latest significant bit is 1
            ans[i] = ans[i >> 1] + (i & 1)

        return ans
