# https://leetcode.com/problems/arithmetic-subarrays/


class Solution:
    """1630. Arithmetic Subarrays

    A sequence of numbers is called **arithmetic** if it consists of at least two
    elements, and the difference between every two consecutive elements is the same.
    More formally, a sequence `s` is arithmetic if and only if `s[i+1] - s[i] == s[1] -
    s[0]` for all valid `i`.

    For example, these are **arithmetic** sequences:

    ```

    1, 3, 5, 7, 9

    7, 7, 7, 7

    3, -1, -5, -9

    ```

    The following sequence is not **arithmetic**:

    ```

    1, 1, 2, 5, 7

    ```

    You are given an array of `n` integers, `nums`, and two arrays of `m` integers each,
    `l` and `r`, representing the `m` range queries, where the `ith` query is the range
    `[l[i], r[i]]`. All the arrays are **0-indexed**.

    Return *a list of* `boolean` *elements* `answer`*, where* `answer[i]` *is* `true`
    *if the subarray* `nums[l[i]], nums[l[i]+1], ... , nums[r[i]]` *can be
    **rearranged** to form an **arithmetic** sequence, and* `false` *otherwise.*
    """

    def check_arithmetic_subarrays(
        self, nums: list[int], l: list[int], r: list[int]
    ) -> list[bool]:
        """Check for arithmetic subarrays.

        Args:
            nums: A list of integers.
            l: First list of integers for queries.
            r: Second list of integers for queries.

        Returns:
            Boolean list indexed to map to subarray[i] which can be rearranged to form
            an arithmetic sequence.
        """

        def is_arithmetic(subarray: list[int]) -> bool:
            """Determine if subarray is arithmetic."""
            subarray.sort()
            diff = subarray[1] - subarray[0]
            # Check if the difference is the same for all consecutive elements.
            for i in range(2, len(subarray)):
                if subarray[i] - subarray[i - 1] != diff:
                    return False
            return True

        result = []
        for i in range(len(l)):
            # Extract the subarray based on the current query.
            subarray = nums[l[i] : r[i] + 1]
            # Check if the subarray can be rearranged to form an arithmetic sequence.
            result.append(is_arithmetic(subarray))

        return result

    checkArithmeticSubarrays = check_arithmetic_subarrays
