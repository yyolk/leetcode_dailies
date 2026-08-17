import importlib.util
from itertools import product
from pathlib import Path

def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260813.py"
    spec = importlib.util.spec_from_file_location("daily_20260813", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()

def brute_longest_repeating(
    s: str, query_characters: str, query_indices: list[int]
) -> list[int]:
    chars = list(s)
    answer: list[int] = []

    for char, idx in zip(query_characters, query_indices, strict=True):
        chars[idx] = char
        best = 1
        run = 1
        for i in range(1, len(chars)):
            if chars[i] == chars[i - 1]:
                run += 1
            else:
                run = 1
            best = max(best, run)
        answer.append(best)

    return answer

def test_longest_substring_of_one_repeating_character_examples(solution):
    assert solution.longestRepeating("babacc", "bcb", [1, 3, 3]) == [3, 3, 4]
    assert solution.longestRepeating("abyzz", "aa", [2, 1]) == [2, 3]

def test_longest_substring_of_one_repeating_character_matches_bruteforce(solution):
    alphabet = ("a", "b")

    for n in range(1, 5):
        for s_tuple in product(alphabet, repeat=n):
            s = "".join(s_tuple)
            for q in range(1, 4):
                for query_indices_tuple in product(range(n), repeat=q):
                    query_indices = list(query_indices_tuple)
                    for query_chars_tuple in product(alphabet, repeat=q):
                        query_characters = "".join(query_chars_tuple)
                        expected = brute_longest_repeating(
                            s, query_characters, query_indices
                        )
                        actual = solution.longestRepeating(
                            s, query_characters, query_indices
                        )
                        assert actual == expected, (
                            s,
                            query_characters,
                            query_indices,
                            expected,
                            actual,
                        )
