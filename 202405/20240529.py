# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/


class Solution:
    """1404. Number of Steps to Reduce a Number in Binary Representation to One

    Given the binary representation of an integer as a string `s`, return *the number of
    steps to reduce it to* `1` *under the following rules*:

    * If the current number is even, you have to divide it by `2`.

    * If the current number is odd, you have to add `1` to it.

    It is guaranteed that you can always reach one for all test cases.

    """

    def num_steps(self, s: str) -> int:
        # Convert the binary string to an integer
        num = int(s, 2)
        steps = 0

        # Continue until the number is reduced to 1
        while num > 1:
            if num % 2 == 0:
                # If the number is even, divide by 2
                num //= 2
            else:
                # If the number is odd, add 1
                num += 1
            # Increment the step counter
            steps += 1

        return steps

    numSteps = num_steps
