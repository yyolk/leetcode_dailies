# https://leetcode.com/problems/count-operations-to-obtain-zero/


class Solution:
    """2169. Count Operations to Obtain Zero

    You are given two non-negative integers num1 and num2.

    In one operation, if num1 >= num2, you must subtract num2 from num1,
    otherwise subtract num1 from num2.

    For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus
    obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5,
    after one operation, num1 = 4 and num2 = 1.

    Return the number of operations required to make either num1 = 0 or
    num2 = 0.
    """
    def count_operations(self, num1: int, num2: int) -> int:
        # Initialize the operation counter
        count = 0
        # Loop until at least one number becomes zero
        while num1 > 0 and num2 > 0:
            # Check if num1 is greater than or equal to num2
            if num1 >= num2:
                # Add the number of times num2 fits into num1
                count += num1 // num2
                # Update num1 to the remainder after subtractions
                num1 %= num2
            else:
                # Add the number of times num1 fits into num2
                count += num2 // num1
                # Update num2 to the remainder after subtractions
                num2 %= num1
        # Return the total count of operations
        return count

    countOperations = count_operations