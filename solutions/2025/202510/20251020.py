# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/


class Solution:
    """2011. Final Value of Variable After Performing Operations

    There is a programming language with only **four** operations and **one** variable
    `X`:

    * `++X` and `X++` **increments** the value of the variable `X` by `1`.

    * `--X` and `X--` **decrements** the value of the variable `X` by `1`.

    Initially, the value of `X` is `0`.

    Given an array of strings `operations` containing a list of operations, return *the
    **final** value of* `X` *after performing all the operations*."""

    def final_value_after_operations(self, operations: list[str]) -> int:
        # Initialize X to 0 as per problem statement
        x = 0
        # Iterate through each operation in the list
        for op in operations:
            # Check for increment operations
            if op == "++X" or op == "X++":
                # Increment X by 1
                x += 1
            # Check for decrement operations
            elif op == "--X" or op == "X--":
                # Decrement X by 1
                x -= 1
        # Return the final value of X after all operations
        return x

    finalValueAfterOperations = final_value_after_operations
