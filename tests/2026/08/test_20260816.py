import importlib.util
from functools import lru_cache
from itertools import product
from pathlib import Path


def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260816.py"
    spec = importlib.util.spec_from_file_location("daily_20260816", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()


def brute_stone_game_ix(stones: list[int]) -> bool:
    counts = [0, 0, 0]
    for stone in stones:
        counts[stone % 3] += 1

    @lru_cache(maxsize=None)
    def dfs(c0: int, c1: int, c2: int, total_mod: int, alice_turn: bool) -> bool:
        total = c0 + c1 + c2
        if total == 0:
            return False

        outcomes: list[bool] = []
        for residue, count in ((0, c0), (1, c1), (2, c2)):
            if count == 0:
                continue

            next_mod = (total_mod + residue) % 3
            if next_mod == 0:
                outcomes.append(not alice_turn)
                continue

            if total == 1:
                outcomes.append(False)
                continue

            next_counts = [c0, c1, c2]
            next_counts[residue] -= 1
            outcomes.append(
                dfs(
                    next_counts[0],
                    next_counts[1],
                    next_counts[2],
                    next_mod,
                    not alice_turn,
                )
            )

        if alice_turn:
            return any(outcomes)

        return all(outcomes)

    return dfs(counts[0], counts[1], counts[2], 0, True)


def test_stone_game_ix_examples():
    solution = load_solution()
    assert solution.stoneGameIX([2, 1]) is True
    assert solution.stoneGameIX([2]) is False
    assert solution.stoneGameIX([5, 1, 2, 4, 3]) is False


def test_stone_game_ix_matches_bruteforce():
    solution = load_solution()
    for n in range(1, 8):
        for stones_tuple in product((1, 2, 3, 4), repeat=n):
            stones = list(stones_tuple)
            expected = brute_stone_game_ix(stones)
            actual = solution.stoneGameIX(stones)
            assert actual == expected, (stones, expected, actual)
