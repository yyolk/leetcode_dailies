# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    """150. Evaluate Reverse Polish Notation

    You are given an array of strings `tokens` that represents an arithmetic expression
    in a [Reverse Polish
    Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

    Evaluate the expression. Return *an integer that represents the value of the
    expression*.

    **Note** that:

    * The valid operators are `'+'`, `'-'`, `'*'`, and `'/'`.

    * Each operand may be an integer or another expression.

    * The division between two integers always **truncates toward zero**.

    * There will not be any division by zero.

    * The input represents a valid arithmetic expression in a reverse polish notation.

    * The answer and all the intermediate calculations can be represented in a
    **32-bit** integer.

    """

    def eval_r_p_n(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
                # If the token is a number, push it onto the stack
                stack.append(int(token))
            else:
                # If the token is an operator, pop the required number of operands from the stack,
                # perform the operation, and push the result back onto the stack.
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    # Handle division by zero case
                    if operand2 == 0:
                        return "Error: Division by zero"
                    stack.append(int(operand1 / operand2))

        # The final result should be on the top of the stack
        return stack[0]

    evalRPN = eval_r_p_n
