# https://leetcode.com/problems/parsing-a-boolean-expression/
from collections import deque


class Solution:
    """1106. Parsing A Boolean Expression

    A **boolean expression** is an expression that evaluates to either `true` or
    `false`. It can be in one of the following shapes:

    * `'t'` that evaluates to `true`.

    * `'f'` that evaluates to `false`.

    * `'!(subExpr)'` that evaluates to **the logical NOT** of the inner expression
    `subExpr`.

    * `'&(subExpr1, subExpr2, ..., subExprn)'` that evaluates to **the logical AND** of
    the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.

    * `'|(subExpr1, subExpr2, ..., subExprn)'` that evaluates to **the logical OR** of
    the inner expressions `subExpr1, subExpr2, ..., subExprn` where `n >= 1`.

    Given a string `expression` that represents a **boolean expression**, return *the
    evaluation of that expression*.

    It is **guaranteed** that the given expression is valid and follows the given rules.

    """

    def parse_bool_expr(self, expression: str) -> bool:
        st = deque()
        for c in expression:
            # Ignore commas and opening parentheses as they don't affect logical evaluation
            if c == "," or c == "(":
                continue

            # Push boolean values or operators onto the stack
            if c in ["t", "f", "!", "&", "|"]:
                st.append(c)

            # Evaluate the expression when encountering a closing parenthesis
            elif c == ")":
                has_true = False
                has_false = False

                # Pop and check all values until an operator is found
                while st[-1] not in ["!", "&", "|"]:
                    top_value = st.pop()
                    if top_value == "t":
                        has_true = True
                    elif top_value == "f":
                        has_false = True

                # Pop the operator
                op = st.pop()

                # Evaluate based on the operator
                if op == "!":
                    # NOT operation: if there was no 't', it's 't', otherwise 'f'
                    st.append("t" if not has_true else "f")
                elif op == "&":
                    # AND operation: 'f' if there's any 'f', else 't'
                    st.append("f" if has_false else "t")
                else:  # op == "|"
                    # OR operation: 't' if there's any 't', else 'f'
                    st.append("t" if has_true else "f")

        # The final result is whether the last item on the stack is 't'
        return st[-1] == "t"

    parseBoolExpr = parse_bool_expr
