import random
from itertools import combinations

def brute_valid_sequence(word1: str, word2: str) -> list[int]:
    n = len(word1)
    m = len(word2)
    best = None
    for seq in combinations(range(n), m):
        formed = "".join(word1[i] for i in seq)
        diff = sum(a != b for a, b in zip(formed, word2))
        if diff <= 1:
            candidate = list(seq)
            if best is None or candidate < best:
                best = candidate
    return best if best is not None else []

def test_find_lexicographically_smallest_valid_sequence_examples(solution):
    assert solution.validSequence("vbcca", "abc") == [0, 1, 2]
    assert solution.validSequence("bacdc", "abc") == [1, 2, 4]
    assert solution.validSequence("aaaaaa", "aaabc") == []

def test_find_lexicographically_smallest_valid_sequence_matches_bruteforce_small(solution):
    alphabet = "abc"
    rng = random.Random(0)
    for n in range(2, 9):
        for m in range(1, n):
            for _ in range(150):
                word1 = "".join(rng.choice(alphabet) for _ in range(n))
                word2 = "".join(rng.choice(alphabet) for _ in range(m))
                expected = brute_valid_sequence(word1, word2)
                actual = solution.validSequence(word1, word2)
                assert actual == expected, (word1, word2, expected, actual)
