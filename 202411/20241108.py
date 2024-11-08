# https://leetcode.com/problems/maximum-xor-for-each-query/


class Solution:
    """1829. Maximum XOR for Each Query

    You are given a **sorted** array `nums` of `n` non\\-negative integers and an integer
    `maximum_bit`. You want to perform the following query `n` **times**:

    1. Find a non\\-negative integer `k < 2maximum_bit` such that `nums[0] XOR nums[1]
    XOR ... XOR nums[nums.length-1] XOR k` is **maximized**. `k` is the answer to the
    `ith` query.

    2. Remove the **last** element from the current array `nums`.

    Return *an array* `answer`*, where* `answer[i]` *is the answer to the* `ith`
    *query*.

    """

    def get_maximum_xor(self, nums: list[int], maximum_bit: int) -> list[int]: ...

    getMaximumXor = get_maximum_xor
