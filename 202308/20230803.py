# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# TODO: Time travel submission 


class Solution:
    """17. Letter Combinations of a Phone Number

    Given a string containing digits from `2-9` inclusive, return all possible letter
    combinations that the number could represent. Return the answer in **any order**.

    A mapping of digits to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.

    ![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

    """

    def letter_combinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        
        # Define the mapping of digits to letters
        mapping = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        # Recursive function to generate combinations
        def generate_combinations(index, path):
            if index == len(digits):
                combinations.append(path)
                return
            
            for letter in mapping[digits[index]]:
                generate_combinations(index + 1, path + letter)

        combinations = []
        generate_combinations(0, '')
        return combinations

    letterCombinations = letter_combinations