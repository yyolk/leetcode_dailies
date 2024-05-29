# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/


class Solution:
    """1404. Number of Steps to Reduce a Number in Binary Representation to One

    Given the binary representation of an integer as a string `s`, return *the number of
    steps to reduce it to* `1` *under the following rules*:

    * If the current number is even, you have to divide it by `2`.

    * If the current number is odd, you have to add `1` to it.

    It is guaranteed that you can always reach one for all test cases.

    """

    def num_steps(self, s: str) -> int: ...

    numSteps = num_steps
