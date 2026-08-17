import importlib.util
from pathlib import Path


def load_solution():
    root = Path(__file__).resolve().parents[3]
    path = root / "solutions" / "2026" / "202608" / "20260803.py"
    spec = importlib.util.spec_from_file_location("daily_20260803", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()


def test_stone_game_iii_examples():
    solution = load_solution()
    assert solution.stoneGameIII([1, 2, 3, 7]) == "Bob"
    assert solution.stoneGameIII([1, 2, 3, -9]) == "Alice"
    assert solution.stoneGameIII([1, 2, 3, 6]) == "Tie"
