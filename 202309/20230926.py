# https://leetcode.com/problems/remove-duplicate-letters/


class Solution:
    """316. Remove Duplicate Letters

    Given a string `s`, remove duplicate letters so that every letter appears once and only
    once. You must make sure your result is **the smallest in lexicographical order** among
    all possible results.

    Note:
        This question is the same as 1081
        https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
    """

    def removeDuplicateLetters(self, s: str) -> str:
        """Removes Duplicate letters so that every lettera appears once

        Proposed solution using set and comparing to previously seen characters for
        lexicographically order.

        Args:
            s (str): input string with duplicate letters

        Returns:
            (str): de-duped input string with the smallest lexicographical order
        """
        # Create an empty list to store chars in the desired order
        stack = []
        # Set to keep track of characters that have already been included in result
        seen = set()
        # Create dictionary to store last occurence index of each char
        last_occurrence = {char: i for i, char in enumerate(s)}

        # Iterate through the input string
        for i, char in enumerate(s):
            # Check if the char has not been included in the result
            if char not in seen:
                # Check whether there are chars in the stack that should be removed
                while stack and char < stack[-1] and i < last_occurrence[stack[-1]]:
                    # Remove chars from stack and update the seen set
                    seen.remove(stack.pop())

                # Add the current char to the seen set and push it onto the stack
                seen.add(char)
                stack.append(char)

        # Join the chars in the stack to obtain the smallest lexicographical result
        return "".join(stack)
