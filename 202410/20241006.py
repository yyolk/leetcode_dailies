# https://leetcode.com/problems/sentence-similarity-iii/


class Solution:
    """1813. Sentence Similarity III

    You are given two strings `sentence1` and `sentence2`, each representing a
    **sentence** composed of words. A sentence is a list of **words** that are separated
    by a **single** space with no leading or trailing spaces. Each word consists of only
    uppercase and lowercase English characters.

    Two sentences `s1` and `s2` are considered **similar** if it is possible to insert
    an arbitrary sentence (*possibly empty*) inside one of these sentences such that the
    two sentences become equal. **Note** that the inserted sentence must be separated
    from existing words by spaces.

    For example,

    * `s1 = "Hello Jane"` and `s2 = "Hello my name is Jane"` can be made equal by
    inserting `"my name is"` between `"Hello"` and `"Jane"` in s1\\.

    * `s1 = "Frog cool"` and `s2 = "Frogs are cool"` are **not** similar, since although
    there is a sentence `"s are"` inserted into `s1`, it is not separated from `"Frog"`
    by a space.

    Given two sentences `sentence1` and `sentence2`, return **true** if `sentence1` and
    `sentence2` are **similar**. Otherwise, return **false**.

    """

    def are_sentences_similar(self, sentence1: str, sentence2: str) -> bool:
        # Split the sentences into lists of words
        words1 = sentence1.split()
        words2 = sentence2.split()

        # If sentences are identical or one is empty
        if words1 == words2 or not words1 or not words2:
            return True

        # Ensure words1 is the shorter or equal length sentence for simplicity
        if len(words1) > len(words2):
            words1, words2 = words2, words1

        i, j = 0, len(words1) - 1
        # Check if words1 is a prefix of words2
        while i < len(words1) and words1[i] == words2[i]:
            i += 1
        # Check if words1 is a suffix of words2
        while j >= 0 and words1[j] == words2[j + (len(words2) - len(words1))]:
            j -= 1

        # If we've matched all of words1, then it's similar due to insertion in the middle or at edges
        if i > j:
            return True

        return False

    areSentencesSimilar = are_sentences_similar
