# https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/

class Solution:
    """3720. Lexicographically Smallest Permutation Greater Than Target

    You are given two strings s and target, both having length n, consisting of
    lowercase English letters.

    Return the lexicographically smallest permutation of s that is strictly
    greater than target. If no permutation of s is lexicographically strictly
    greater than target, return an empty string.

    A string a is lexicographically strictly greater than a string b (of the
    same length) if in the first position where a and b differ, string a has a
    letter that appears later in the alphabet than the corresponding letter in
    b.

    Constraints:
    * 1 <= s.length == target.length <= 300
    * s and target consist of only lowercase English letters.
    """
    def lex_greater_permutation(self, s: str, target: str) -> str:
        # Count remaining occurrences of each letter in s.
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        def smallest_greater(counts: list[int], ch: str) -> int:
            # Alphabet index of the smallest unused letter > ch, else -1.
            for i in range(ord(ch) - ord("a") + 1, 26):
                if counts[i]:
                    return i
            return -1

        # Match target's prefix and record the rightmost index we can raise.
        work = freq[:]
        pivot = -1
        for i, ch in enumerate(target):
            if smallest_greater(work, ch) != -1:
                pivot = i
            idx = ord(ch) - ord("a")
            if work[idx] == 0:
                break
            work[idx] -= 1

        # No position can be increased using a permutation of s.
        if pivot == -1:
            return ""

        # Keep the matched prefix, then place the smallest letter > target[pivot].
        answer: list[str] = []
        for i in range(pivot):
            answer.append(target[i])
            freq[ord(target[i]) - ord("a")] -= 1

        raised = smallest_greater(freq, target[pivot])
        answer.append(chr(raised + ord("a")))
        freq[raised] -= 1

        # Append leftover letters in non-decreasing order.
        for i in range(26):
            if freq[i]:
                answer.append(chr(i + ord("a")) * freq[i])

        return "".join(answer)

    lexGreaterPermutation = lex_greater_permutation
