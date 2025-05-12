# https://leetcode.com/problems/finding-3-digit-even-numbers/
from itertools import permutations


class Solution:
    """2094. Finding 3-Digit Even Numbers

    You are given an integer array `digits`, where each element is a digit. The array
    may contain duplicates.

    You need to find **all** the **unique** integers that follow the given requirements:

    * The integer consists of the **concatenation** of **three** elements from `digits`
    in **any** arbitrary order.

    * The integer does not have **leading zeros**.

    * The integer is **even**.

    For example, if the given `digits` were `[1, 2, 3]`, integers `132` and `312` follow
    the requirements.

    Return *a **sorted** array of the unique integers.*"""

    def find_even_numbers(self, digits: list[int]) -> list[int]:
        # Set to store unique valid numbers
        result = set()
        
        # Generate all permutations of 3 digits
        for perm in permutations(digits, 3):
            # Check conditions:
            # 1. No leading zeros (first digit != 0)
            # 2. Number is even (last digit % 2 == 0)
            if perm[0] != 0 and perm[2] % 2 == 0:
                # Form the three-digit number
                num = 100 * perm[0] + 10 * perm[1] + perm[2]
                result.add(num)
        
        # Return sorted list of unique numbers
        return sorted(list(result))

    findEvenNumbers = find_even_numbers
