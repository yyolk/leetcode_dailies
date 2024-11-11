# https://leetcode.com/problems/prime-subtraction-operation/


class Solution:
    """2601. Prime Subtraction Operation

    You are given a **0\\-indexed** integer array `nums` of length `n`.

    You can perform the following operation as many times as you want:

    * Pick an index `i` that you haven’t picked before, and pick a prime `p` **strictly
    less than** `nums[i]`, then subtract `p` from `nums[i]`.

    Return *true if you can make `nums` a strictly increasing array using the above
    operation and false otherwise.*

    A **strictly increasing array** is an array whose each element is strictly greater
    than its preceding element.

    """

    def prime_sub_operation(self, nums: list[int]) -> bool: ...

    primeSubOperation = prime_sub_operation
