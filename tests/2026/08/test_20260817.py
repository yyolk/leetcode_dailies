import importlib.util
from functools import lru_cache
from itertools import product
from pathlib import Path

def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260817.py"
    spec = importlib.util.spec_from_file_location("daily_20260817", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()

def brute_stone_game_v(stone_value: list[int]) -> int:
    prefix = [0]
    for value in stone_value:
        prefix.append(prefix[-1] + value)

    def range_sum(left: int, right: int) -> int:
        return prefix[right + 1] - prefix[left]

    @lru_cache(maxsize=None)
    def dfs(left: int, right: int) -> int:
        if left == right:
            return 0

        best = 0
        for split in range(left, right):
            left_sum = range_sum(left, split)
            right_sum = range_sum(split + 1, right)
            if left_sum < right_sum:
                best = max(best, left_sum + dfs(left, split))
            elif left_sum > right_sum:
                best = max(best, right_sum + dfs(split + 1, right))
            else:
                best = max(
                    best,
                    left_sum + dfs(left, split),
                    right_sum + dfs(split + 1, right),
                )
        return best

    return dfs(0, len(stone_value) - 1)

def test_stone_game_v_examples(solution):
    assert solution.stoneGameV([6, 2, 3, 4, 5, 5]) == 18
    assert solution.stoneGameV([7, 7, 7, 7, 7, 7, 7]) == 28
    assert solution.stoneGameV([4]) == 0

def test_stone_game_v_matches_bruteforce(solution):
    for n in range(1, 8):
        for values_tuple in product((1, 2, 3, 4), repeat=n):
            stone_value = list(values_tuple)
            expected = brute_stone_game_v(stone_value)
            actual = solution.stoneGameV(stone_value)
            assert actual == expected, (stone_value, expected, actual)
