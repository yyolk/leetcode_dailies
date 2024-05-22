# https://leetcode.com/problems/palindrome-partitioning/


class Solution:
    """131. Palindrome Partitioning

    Given a string `s`, partition `s` such that every substring of the partition is a
    **palindrome**. Return *all possible palindrome partitioning of* `s`.

    """

    def partition(self, s: str) -> list[list[str]]:
        # Helper function to check if a substring is a palindrome
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        # Backtracking function to find all partitions
        def backtrack(start: int, path: list):
            # If we have reached the end of the string, add the current path to results
            if start == len(s):
                result.append(path[:])
                return
            
            # Explore all possible partitions starting from 'start'
            for end in range(start + 1, len(s) + 1):
                # Get the substring
                substring = s[start:end]
                # If the substring is a palindrome, recurse with the new start position
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result