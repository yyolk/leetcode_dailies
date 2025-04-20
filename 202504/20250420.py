# https://leetcode.com/problems/rabbits-in-forest/


class Solution:
    """781. Rabbits in Forest

    There is a forest with an unknown number of rabbits. We asked n rabbits **"How many
    rabbits have the same color as you?"** and collected the answers in an integer array
    `answers` where `answers[i]` is the answer of the `ith` rabbit.

    Given the array `answers`, return *the minimum number of rabbits that could be in
    the forest*."""

    def num_rabbits(self, answers: list[int]) -> int:
        """
        Calculate the minimum number of rabbits in the forest based on their answers.

        Args:
            answers (list[int]): Array where answers[i] is the number of other rabbits
                                 with the same color as the ith rabbit.

        Returns:
            int: The minimum possible number of rabbits in the forest.
        """
        # Count the frequency of each answer
        count = collections.Counter(answers)
        
        total = 0
        # Process each unique answer k
        for k, m_k in count.items():
            # Group size is k + 1 (including the rabbit itself)
            group_size = k + 1
            # Number of groups needed, using ceiling division
            groups = (m_k + group_size - 1) // group_size
            # Total rabbits for this answer = number of groups * group size
            total += groups * group_size
        
        return total

    numRabbits = num_rabbits
