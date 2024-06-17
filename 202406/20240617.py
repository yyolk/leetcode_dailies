# https://leetcode.com/problems/sum-of-square-numbers/


class Solution:
    """633. Sum of Square Numbers

    Given a non-negative integer `c`, decide whether there're two integers `a` and `b`
    such that `a2 + b2 = c`.

    """

    def judge_square_sum(self, c: int) -> bool:
        # Initialize two pointers, one starting from 0 and the other from the square root of c
        a = 0
        b = int(c**0.5)
        
        # Use a while loop to check the sum of squares of the two pointers
        while a <= b:
            current_sum = a * a + b * b
            
            # If the current sum equals c, we have found such integers a and b
            if current_sum == c:
                return True
            # If the current sum is less than c, increment the lower pointer
            elif current_sum < c:
                a += 1
            # If the current sum is greater than c, decrement the upper pointer
            else:
                b -= 1
        
        # If no such pair is found, return False
        return False

    judgeSquareSum = judge_square_sum
