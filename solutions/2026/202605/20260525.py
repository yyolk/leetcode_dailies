# https://leetcode.com/problems/jump-game-vii/


class Solution:
    """1871. Jump Game VII

    You are given a **0-indexed** binary string `s` and two integers `min_jump` and
    `max_jump`. In the beginning, you are standing at index `0`, which is equal to
    `'0'`. You can move from index `i` to index `j` if the following conditions are
    fulfilled:

    * `i + min_jump <= j <= min(i + max_jump, s.length - 1)`, and

    * `s[j] == '0'`.

    Return `true` *if you can reach index* `s.length - 1` *in* `s`*, or* `false`
    *otherwise.*"""

    def can_reach(self, s: str, min_jump: int, max_jump: int) -> bool: ...

    canReach = can_reach
