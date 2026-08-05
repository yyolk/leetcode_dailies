# https://leetcode.com/problems/remove-methods-from-project/


class Solution:
    """3310. Remove Methods From Project

    You are maintaining a project that has `n` methods numbered from `0` to `n - 1`.

    You are given two integers `n` and `k`, and a 2D integer array `invocations`, where
    `invocations[i] = [ai, bi]` indicates that method `ai` invokes method `bi`.

    There is a known bug in method `k`. Method `k`, along with any method invoked by it,
    either **directly** or **indirectly**, are considered **suspicious** and we aim to
    remove them.

    A group of methods can only be removed if no method **outside** the group invokes
    any methods **within** it.

    Return an array containing all the remaining methods after removing all the
    **suspicious** methods. You may return the answer in *any order*. If it is not
    possible to remove **all** the suspicious methods, **none** should be removed.

    Constraints:

    * `1 <= n <= 105`

    * `0 <= k <= n - 1`

    * `0 <= invocations.length <= 2 * 105`

    * `invocations[i] == [ai, bi]`

    * `0 <= ai, bi <= n - 1`

    * `ai != bi`

    * `invocations[i] != invocations[j]`"""

    def remaining_methods(
        self, n: int, k: int, invocations: list[list[int]]
    ) -> list[int]:
        """...

        Proposed solution ...

        Args:
            n (int): ...
            k (int): ...
            invocations (list of list of int): ...

        Returns:
            list of int: ..."""
        ...

    remainingMethods = remaining_methods
