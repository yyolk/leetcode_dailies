import random
def brute_stone_game_ii(piles: list[int]) -> int:
    from functools import lru_cache

    n = len(piles)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + piles[i]

    @lru_cache(maxsize=None)
    def solve(i: int, m: int) -> int:
        if i >= n:
            return 0
        best = 0
        total = 0
        for x in range(1, min(2 * m, n - i) + 1):
            total += piles[i + x - 1]
            best = max(best, total + (suffix[i + x] - solve(i + x, max(m, x))))
        return best

    return solve(0, 1)

def test_stone_game_ii_examples(solution):
    assert solution.stoneGameII([2, 7, 9, 4, 4]) == 10
    assert solution.stoneGameII([1, 2, 3, 4, 5, 100]) == 104

def test_stone_game_ii_matches_bruteforce_small_random_inputs(solution):
    rng = random.Random(0)
    for n in range(1, 10):
        for _ in range(120):
            piles = [rng.randint(1, 9) for _ in range(n)]
            expected = brute_stone_game_ii(piles)
            actual = solution.stoneGameII(piles)
            assert actual == expected, (piles, expected, actual)
