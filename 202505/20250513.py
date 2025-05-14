# https://leetcode.com/problems/total-characters-in-string-after-transformations-i/
MODULO_CONSTANT = 1_000_000_007
# Initialize a list to store precomputed dynamic programming values for transformations
dynamic_programming_array = [1] * (100_000 + 26)

# Precompute the transformation length multipliers for each step beyond the initial 26 characters
for transformation_index in range(26, len(dynamic_programming_array)):
    # Each value is the sum of the multipliers 25 and 26 steps back, modulo the constant
    dynamic_programming_array[transformation_index] = (
        dynamic_programming_array[transformation_index - 26]
        + dynamic_programming_array[transformation_index - 25]
    ) % MODULO_CONSTANT


class Solution:
    """3335. Total Characters in String After Transformations I

    You are given a string `s` and an integer `t`, representing the number of
    **transformations** to perform. In one **transformation**, every character in `s` is
    replaced according to the following rules:

    * If the character is `'z'`, replace it with the string `"ab"`.

    * Otherwise, replace it with the **next** character in the alphabet. For example,
    `'a'` is replaced with `'b'`, `'b'` is replaced with `'c'`, and so on.

    Return the **length** of the resulting string after **exactly** `t` transformations.

    Since the answer may be very large, return it **modulo** `109 + 7`."""

    def length_after_transformations(
        self, input_string: str, number_of_transformations: int
    ) -> int:
        # Initialize a variable to accumulate the total length after transformations
        total_length_after_transformations = 0

        # Count the frequency of each character in the input string using a Counter
        character_frequency_counter = Counter(input_string)

        # Iterate over each unique character and its frequency in the input string
        for (
            current_character,
            frequency_of_character,
        ) in character_frequency_counter.items():
            # Calculate the index in the dynamic programming array based on character position and transformations
            # ord(current_character) - 97 maps 'a' to 0, 'b' to 1, ..., 'z' to 25
            transformation_lookup_index = (
                ord(current_character) - 97
            ) + number_of_transformations

            # Update total length by adding the product of frequency and the precomputed length multiplier
            total_length_after_transformations = (
                total_length_after_transformations
                + frequency_of_character
                * dynamic_programming_array[transformation_lookup_index]
            ) % MODULO_CONSTANT

        return total_length_after_transformations

    lengthAfterTransformations = length_after_transformations
