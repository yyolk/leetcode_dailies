# https://leetcode.com/problems/sequential-digits/


class Solution:
    """1291. Sequential Digits

    An integer has *sequential digits* if and only if each digit in the number is one
    more than the previous digit.

    Return a **sorted** list of all the integers in the range `[low, high]` inclusive
    that have sequential digits.

    """

    def sequential_digits(self, low: int, high: int) -> list[int]:
        result = []
        
        # Helper function to generate sequential digits recursively
        def generate_sequential(number, current_digit):
            # Check if the generated number is within the given range
            if low <= number <= high:
                result.append(number)
            
            # If the current digit is less than 9, generate the next sequential digit
            if current_digit < 9:
                new_digit = current_digit + 1
                next_number = number * 10 + new_digit
                # Recursive call with the next digit and number
                generate_sequential(next_number, new_digit)
        
        # Start generating sequential digits for each starting digit from 1 to 9
        for i in range(1, 10):
            generate_sequential(i, i)
        
        # Return the sorted list of sequential digits
        return sorted(result)

    sequentialDigits = sequential_digits
