# https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/
from collections import deque


class Solution:
    """3170. Lexicographically Minimum String After Removing Stars

    You are given a string `s`. It may contain any number of `"*"` characters. Your task
    is to remove all `"*"` characters.

    While there is a `"*"`, do the following operation:

    * Delete the leftmost `"*"` and the **smallest** non-`"*"` character to its *left*.
    If there are several smallest characters, you can delete any of them.

    Return the lexicographically smallest resulting string after removing all `"*"`
    characters."""

    def clear_stars(self, input_string: str) -> str:
        # Initialize a list of deques to store indices for each character 'a' to 'z'
        character_position_queues = [deque() for _ in range(26)]
        # Create a list to mark which indices should be removed (0 = keep, 1 = remove)
        indices_to_remove = [0] * len(input_string)

        # Start iterating through the string with an index
        current_index = 0
        while current_index < len(input_string):
            # Get the current character and calculate its position in the alphabet
            current_char_position = ord(input_string[current_index]) - ord("a")
            # Add the current index to the queue for this character if it's not a '*'
            if input_string[current_index] != "*":
                character_position_queues[current_char_position].append(current_index)
            # Move to the next character
            current_index += 1

            # Initialize a counter for consecutive '*' characters
            star_count = 0
            # Count the number of consecutive '*' characters
            while current_index < len(input_string) and input_string[current_index] == "*":
                star_count += 1
                current_index += 1

            # If there were any '*' characters, process them
            if star_count > 0:
                # Iterate through characters 'a' to 'z' to find the smallest available
                for char_index in range(26):
                    # Continue removing characters while the queue is not empty
                    while character_position_queues[char_index]:
                        # Remove the most recently added index for this character
                        removed_index = character_position_queues[char_index].pop()
                        # Mark this index for removal
                        indices_to_remove[removed_index] = 1
                        # Decrease the star count
                        star_count -= 1
                        # Stop if all stars have been processed
                        if star_count == 0:
                            break
                    # Stop if all stars have been processed
                    if star_count == 0:
                        break

        # Initialize a list to build the final result
        result_characters = []
        # Iterate through the string to construct the result
        for index in range(len(input_string)):
            # Include characters that are not '*' and not marked for removal
            if input_string[index] != "*" and indices_to_remove[index] == 0:
                result_characters.append(input_string[index])

        # Join the characters into a single string and return it
        return "".join(result_characters)

    clearStars = clear_stars
