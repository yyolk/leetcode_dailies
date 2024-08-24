# https://leetcode.com/problems/find-the-closest-palindrome/


class Solution:
    """564. Find the Closest Palindrome

    Given a string `n` representing an integer, return *the closest integer (not
    including itself), which is a palindrome*. If there is a tie, return ***the smaller
    one***.

    The closest is defined as the absolute difference minimized between two integers.

    """

    def nearest_palindromic(self, n: str) -> str:
        length = len(n)
        # Edge case: if n is a single digit, return n-1
        if length == 1:
            return str(int(n) - 1)
        
        # Create the candidates
        candidates = set()
        
        # The first candidate is by reflecting the first half of the string n
        first_half = n[:(length + 1) // 2]
        for diff in [-1, 0, 1]:
            # Generate the first half with the possible adjustment (e.g., decrement or increment)
            new_first_half = str(int(first_half) + diff)
            if len(new_first_half) != len(first_half):
                continue
            # Create a new palindrome by reflecting the adjusted first half
            if length % 2 == 0:
                candidate = new_first_half + new_first_half[::-1]
            else:
                candidate = new_first_half + new_first_half[:-1][::-1]
            candidates.add(candidate)
        
        # Edge cases
        candidates.add('9' * (length - 1))  # 999...999 (one digit less)
        candidates.add('1' + '0' * (length - 1) + '1')  # 100...001
        
        # Remove n itself from candidates
        candidates.discard(n)
        
        # Convert the candidates to integers and find the closest palindrome
        closest = None
        min_diff = float('inf')
        for candidate in candidates:
            diff = abs(int(candidate) - int(n))
            if diff < min_diff or (diff == min_diff and int(candidate) < int(closest)):
                closest = candidate
                min_diff = diff
        
        return closest        

    nearestPalindromic = nearest_palindromic
