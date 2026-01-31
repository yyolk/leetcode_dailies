# https://leetcode.com/problems/find-smallest-letter-greater-than-target


class Solution:
    """744. Find Smallest Letter Greater Than Target
    
    You are given an array of characters letters that is sorted in non-decreasing
    order, and a character target. There are at least two different characters in
    letters.
    
    Return the smallest character in letters that is lexicographically greater
    than target. If such a character does not exist, return the first character
    in letters.
    """
    def next_greatest_letter(self, letters: list[str], target: str) -> str:
        n = len(letters)
        left = 0
        right = n - 1
        
        # Binary search for the leftmost position where letters[i] > target
        while left <= right:
            mid = left + (right - left) // 2
            
            if letters[mid] <= target:
                # Everything <= mid is not greater than target; discard left half
                left = mid + 1
            else:
                # letters[mid] > target; potential answer, check left for smaller
                right = mid - 1
        
        # left is now the smallest index with letters[left] > target,
        # or n if no such character exists
        return letters[left] if left < n else letters[0]

    nextGreatestLetter = next_greatest_letter