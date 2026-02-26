# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one


class Solution:
    """1404. Number of Steps to Reduce a Number in Binary Representation to One
    
    Given the binary representation of an integer as a string s, return the
    number of steps to reduce it to 1 under the following rules:
    
    - If the current number is even, divide it by 2.
    - If the current number is odd, add 1 to it.
    
    It is guaranteed that you can always reach 1 for all test cases.
    """
    def num_steps(self, s: str) -> int:
        steps = 0
        carry = 0
        # Process from LSB (end) to second-MSB (skip leading '1')
        for bit in s[:0:-1]:
            # Apply carry if pending from prior add-1
            if carry:
                if bit == "0":
                    bit = "1"
                    carry = 0
                else:
                    bit = "0"
                    # carry remains 1
            # Effective bit is 1: must add 1 before divide (sets carry)
            if bit == "1":
                steps += 1  # add-1 operation
                carry = 1
            steps += 1  # divide-by-2 operation for this bit
        # Final carry after MSB requires one extra add-1 (and implied divide)
        if carry:
            steps += 1
        return steps

    numSteps = num_steps