# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/


class Solution:
    """2433. Find The Original Array of Prefix Xor

    You are given an **integer** array `pref` of size `n`. Find and return *the array*
    `arr` *of size* `n` *that satisfies*:

    * `pref[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]`.

    Note that `^` denotes the **bitwise-xor** operation.

    It can be proven that the answer is **unique**.
    """

    def find_array(self, pref: list[int]) -> list[int]:
        """Finds and returns the original array `arr` of size `n` that satisfies the given conditions.

        Proposed solution using dyanmic programming.

        Args:
            pref: An integer list of size `n` representing the prefix XOR values.

        Returns:
            The original array `arr` of size `n`.

        Example:
            >>> solution = Solution()
            >>> solution.find_array([1, 3, 2, 6, 4])
            [1, 2, 3, 4, 5]

        Note:
            The answer is guaranteed to be unique.
        """
        n = len(pref)
        # Initialize arr with 0s
        arr = [0] * (n + 1)
        # Initialize the result array
        result = [0] * n

        for i in range(n):
            # Calculate the current element of the result array
            result[i] = pref[i] ^ arr[i]

            # Update the arr array for the next iteration
            arr[i + 1] = arr[i] ^ result[i]

        return result

    findArray = find_array
