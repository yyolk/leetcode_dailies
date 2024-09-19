# https://leetcode.com/problems/different-ways-to-add-parentheses/


class Solution:
    """241. Different Ways to Add Parentheses

    Given a string `expression` of numbers and operators, return *all possible results
    from computing all the different possible ways to group numbers and operators*. You
    may return the answer in **any order**.

    The test cases are generated such that the output values fit in a 32\\-bit integer
    and the number of different results does not exceed `104`.

    """

    def diff_ways_to_compute(self, expression: str) -> list[int]:
        def compute(left, right, op):
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
        
        # If the expression is just a number, return it as a single-element list
        if expression.isdigit():
            return [int(expression)]
        
        results = []
        for i, char in enumerate(expression):
            if char in ["+", "-", "*"]:
                # Recursively compute results for left and right subexpressions
                left_results = self.diff_ways_to_compute(expression[:i])
                right_results = self.diff_ways_to_compute(expression[i+1:])
                
                # Combine all possible results
                for left in left_results:
                    for right in right_results:
                        results.append(compute(left, right, char))
        
        return results

    diffWaysToCompute = diff_ways_to_compute
