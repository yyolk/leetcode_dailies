from itertools import product


def brute_maximum_length_substring(s: str) -> int:
    best = 0
    for left in range(len(s)):
        counts: dict[str, int] = {}
        for right in range(left, len(s)):
            char = s[right]
            counts[char] = counts.get(char, 0) + 1
            if counts[char] > 2:
                break
            best = max(best, right - left + 1)
    return best


def test_maximum_length_substring_with_two_occurrences_examples(solution):
    assert solution.maximumLengthSubstring("bcbbbcba") == 4
    assert solution.maximumLengthSubstring("aaaa") == 2


def test_maximum_length_substring_with_two_occurrences_matches_bruteforce(solution):
    for n in range(2, 8):
        for s_tuple in product(("a", "b", "c"), repeat=n):
            s = "".join(s_tuple)
            expected = brute_maximum_length_substring(s)
            actual = solution.maximumLengthSubstring(s)
            assert actual == expected, (s, expected, actual)
