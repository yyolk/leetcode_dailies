# https://leetcode.com/problems/bag-of-tokens/


class Solution:
    """948. Bag of Tokens

    You start with an initial **power** of `power`, an initial **score** of `0`, and a
    bag of tokens given as an integer array `tokens`, where each `tokens[i]` donates the
    value of token*i*.

    Your goal is to **maximize** the total **score** by strategically playing these
    tokens. In one move, you can play an **unplayed** token in one of the two ways (but
    not both for the same token):

    * **Face-up**: If your current power is **at least** `tokens[i]`, you may play
    token*i*, losing `tokens[i]` power and gaining `1` score.

    * **Face-down**: If your current score is **at least** `1`, you may play token*i*,
    gaining `tokens[i]` power and losing `1` score.

    Return *the **maximum** possible score you can achieve after playing **any** number
    of tokens*.

    """

    def bag_of_tokens_score(self, tokens: list[int], power: int) -> int:
        # Sorting the tokens array to optimize the strategy
        tokens.sort()

        max_score = 0
        current_score = 0
        left = 0
        right = len(tokens) - 1

        # Two-pointer approach to iterate through the tokens array
        while left <= right:
            # If current power is enough to play token face-up
            if power >= tokens[left]:
                power -= tokens[left]
                current_score += 1
                left += 1
                # Update the maximum score achieved so far
                max_score = max(max_score, current_score)
            # If current score is greater than 0, play token face-down
            elif current_score > 0:
                power += tokens[right]
                current_score -= 1
                right -= 1
            else:
                # If neither face-up nor face-down is possible, break the loop
                break

        # Return the maximum score achievable
        return max_score

    bagOfTokensScore = bag_of_tokens_score
