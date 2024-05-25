# https://leetcode.com/problems/maximum-score-words-formed-by-letters/


class Solution:
    """1255. Maximum Score Words Formed by Letters

    Given a list of `words`, list of  single `letters` (might be repeating) and `score`
    of every character.

    Return the maximum score of **any** valid set of words formed by using the given
    letters (`words[i]` cannot be used two or more times).

    It is not necessary to use all characters in `letters` and each letter can only be
    used once. Score of letters `'a'`, `'b'`, `'c'`, ... ,`'z'` is given by `score[0]`,
    `score[1]`, ... , `score[25]` respectively.

    """

    def max_score_words(
        self, words: list[str], letters: list[str], score: list[int]
    ) -> int:
        # Function to count the frequency of each letter in a word
        def count_letters(word):
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            return count

        # Function to calculate the score of a subset of words
        def calculate_score(words):
            total_score = 0
            for word in words:
                for char in word:
                    total_score += score[ord(char) - ord("a")]
            return total_score

        # Backtracking function to find the maximum score
        def backtrack(index, current_words, current_count):
            if index == len(words):
                return calculate_score(current_words)

            # Skip the current word
            max_score = backtrack(index + 1, current_words, current_count)

            # Include the current word if possible
            word_count = count_letters(words[index])
            if all(current_count[i] >= word_count[i] for i in range(26)):
                for i in range(26):
                    current_count[i] -= word_count[i]
                current_words.append(words[index])
                max_score = max(
                    max_score, backtrack(index + 1, current_words, current_count)
                )
                current_words.pop()
                for i in range(26):
                    current_count[i] += word_count[i]

            return max_score

        # Initial count of available letters
        letter_count = [0] * 26
        for char in letters:
            letter_count[ord(char) - ord("a")] += 1

        return backtrack(0, [], letter_count)

    maxScoreWords = max_score_words
