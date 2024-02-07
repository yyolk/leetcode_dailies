# https://leetcode.com/problems/group-anagrams/


class Solution:
    """49. Group Anagrams

    Given an array of strings `strs`, group **the anagrams** together. You can return
    the answer in **any order**.

    An **Anagram** is a word or phrase formed by rearranging the letters of a different
    word or phrase, typically using all the original letters exactly once.

    """

    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_groups = {}

        for word in strs:
            sorted_word = "".join(sorted(word))

            if sorted_word in anagram_groups:
                anagram_groups[sorted_word].append(word)
            else:
                anagram_groups[sorted_word] = [word]

        return list(anagram_groups.values())

    groupAnagrams = group_anagrams
