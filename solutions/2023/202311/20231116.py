# https://leetcode.com/problems/find-unique-binary-string/


class Solution:
    """1980. Find Unique Binary String

    Given an array of strings `nums` containing `n` **unique** binary strings each of
    length `n`, return *a binary string of length* `n` *that **does not appear** in*
    `nums`*. If there are multiple answers, you may return **any** of them*.

    Constraints:

        * `n == nums.length`
        * `1 <= n <= 16`
        * `nums[i].length == n`
        * `nums[i]` is either `'0'` or `'1'`.
        * All the strings of `nums` are **unique**.
    """

    def find_different_binary_string(self, nums: list[str]) -> str:
        """Finds a binary string not already included in input nums[].

        Args:
            nums: Input list of binary number strings.
                A binary number represented by 1s and 0s.

        Returns:
            Binary number string not a member of input nums.
        """
        # `n == nums.length == nums[i].length`
        n = len(nums)
        # Our seen set is all distinct binary strings.
        seen = set(nums)

        # When generating binary strings, a string of length n corresponds to a unique
        # decimal number between 0 and 2^n.
        for i in range(2**n):
            # Make int candidate i a binary string and check it's not in seen.
            if (binary_str := format(i, "b").zfill(n)) not in seen:
                return binary_str

    findDifferentBinaryString = find_different_binary_string
