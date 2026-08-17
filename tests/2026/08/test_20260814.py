import importlib.util
from itertools import product
from pathlib import Path

def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260814.py"
    spec = importlib.util.spec_from_file_location("daily_20260814", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()

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
