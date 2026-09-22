# https://leetcode.com/problems/find-x-value-of-array-ii/


class Solution:
    """3525. Find X Value of Array II

    You are given an array of **positive** integers `nums` and a **positive** integer
    `k`. You are also given a 2D array `queries`, where `queries[i] = [indexi, valuei,
    starti, xi]`.

    You are allowed to perform an operation **once** on `nums`, where you can remove any
    **suffix** from `nums` such that `nums` remains **non-empty**.

    The **x-value** of `nums` **for a given** `x` is defined as the number of ways to
    perform this operation so that the **product** of the remaining elements leaves a
    *remainder* of `x` **modulo** `k`.

    For each query in `queries` you need to determine the **x-value** of `nums` for `xi`
    after performing the following actions:

    * Update `nums[indexi]` to `valuei`. Only this step persists for the rest of the
    queries.

    * **Remove** the prefix `nums[0..(starti - 1)]` (where `nums[0..(-1)]` will be used
    to represent the **empty** prefix).

    Return an array `result` of size `queries.length` where `result[i]` is the answer
    for the `ith` query.

    A **prefix** of an array is a subarray that starts from the beginning of the array
    and extends to any point within it.

    A **suffix** of an array is a subarray that starts at any point within the array and
    extends to the end of the array.

    **Note** that the prefix and suffix to be chosen for the operation can be **empty**.

    **Note** that x-value has a *different* definition in this version.

    Constraints:

    * `1 <= nums[i] <= 109`

    * `1 <= nums.length <= 105`

    * `1 <= k <= 5`

    * `1 <= queries.length <= 2 * 104`

    * `queries[i] == [indexi, valuei, starti, xi]`

    * `0 <= indexi <= nums.length - 1`

    * `1 <= valuei <= 109`

    * `0 <= starti <= nums.length - 1`

    * `0 <= xi <= k - 1`"""

    def result_array(
        self, nums: list[int], k: int, queries: list[list[int]]
    ) -> list[int]:
        """...

        Proposed solution ...

        Args:
            nums (list of int): ...
            k (int): ...
            queries (list of list of int): ...

        Returns:
            list of int: ..."""
        ...

    resultArray = result_array
