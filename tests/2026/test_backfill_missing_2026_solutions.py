import importlib.util
import inspect
from pathlib import Path

import pytest


class TreeNode: ...


class ListNode: ...


class Node: ...


class NestedInteger: ...


class ImmutableListNode: ...


class Employee: ...


class Pair: ...


LEETCODE_TYPE_STUBS = {
    "TreeNode": TreeNode,
    "ListNode": ListNode,
    "Node": Node,
    "NestedInteger": NestedInteger,
    "ImmutableListNode": ImmutableListNode,
    "Employee": Employee,
    "Pair": Pair,
}

REPO_ROOT = Path(__file__).resolve().parents[2]
SOLUTIONS_2026_ROOT = REPO_ROOT / "solutions" / "2026"
TESTS_2026_ROOT = REPO_ROOT / "tests" / "2026"


def _missing_solution_date_codes() -> list[str]:
    solution_dates = {path.stem for path in SOLUTIONS_2026_ROOT.rglob("*.py")}
    tested_dates = {
        path.stem.removeprefix("test_")
        for path in TESTS_2026_ROOT.rglob("test_*.py")
        if path.stem.startswith("test_")
        and len(path.stem.removeprefix("test_")) == 8
        and path.stem.removeprefix("test_").isdigit()
    }
    return sorted(solution_dates - tested_dates)


@pytest.mark.parametrize("date_code", _missing_solution_date_codes())
def test_backfill_missing_2026_solution_module(date_code):
    module_path = SOLUTIONS_2026_ROOT / date_code[:6] / f"{date_code}.py"
    spec = importlib.util.spec_from_file_location(f"daily_{date_code}", module_path)
    assert spec is not None and spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    module.__dict__.update(LEETCODE_TYPE_STUBS)
    spec.loader.exec_module(module)

    classes = [
        value
        for value in module.__dict__.values()
        if inspect.isclass(value) and value.__module__ == module.__name__
    ]
    assert classes, f"No classes found in {date_code}"

    has_public_callable_class = False
    for cls in classes:
        public_callables = [
            name
            for name, value in vars(cls).items()
            if callable(value) and not name.startswith("_")
        ]
        if public_callables:
            has_public_callable_class = True
            break

    assert has_public_callable_class, (
        f"No public callable class API found in {date_code}"
    )
