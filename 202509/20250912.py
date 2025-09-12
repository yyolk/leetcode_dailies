# https://leetcode.com/problems/vowels-game-in-a-string/


class Solution:
    """3227. Vowels Game in a String

    Alice and Bob are playing a game on a string.

    You are given a string `s`, Alice and Bob will take turns playing the following game
    where Alice starts **first**:

    * On Alice's turn, she has to remove any **non-empty** substring from `s` that
    contains an **odd** number of vowels.

    * On Bob's turn, he has to remove any **non-empty** substring from `s` that contains
    an **even** number of vowels.

    The first player who cannot make a move on their turn loses the game. We assume that
    both Alice and Bob play **optimally**.

    Return `true` if Alice wins the game, and `false` otherwise.

    The English vowels are: `a`, `e`, `i`, `o`, and `u`."""

    def does_alice_win(self, s: str) -> bool:
        # Define vowels for checking
        vowels = set("aeiou")
        # Count total vowels in the string
        vowel_count = sum(1 for c in s if c in vowels)
        
        # If no vowels, Alice can't make a move (needs odd vowels)
        if vowel_count == 0:
            return False
        # If any vowels exist, Alice can always make a move to force a win
        return True

    doesAliceWin = does_alice_win