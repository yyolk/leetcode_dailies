import importlib.util
from functools import lru_cache
from pathlib import Path


def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260810.py"
    spec = importlib.util.spec_from_file_location("daily_20260810", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()


def brute_winner_square_game(n: int) -> bool:
    @lru_cache(maxsize=None)
    def can_win(stones: int) -> bool:
        i = 1
        while i * i <= stones:
            if not can_win(stones - i * i):
                return True
            i += 1
        return False

    return can_win(n)


def test_stone_game_iv_examples():
    solution = load_solution()
    assert solution.winnerSquareGame(1) is True
    assert solution.winnerSquareGame(2) is False
    assert solution.winnerSquareGame(4) is True


def test_stone_game_iv_matches_bruteforce_small_inputs():
    solution = load_solution()
    for n in range(1, 201):
        expected = brute_winner_square_game(n)
        actual = solution.winnerSquareGame(n)
        assert actual is expected, (n, expected, actual)
