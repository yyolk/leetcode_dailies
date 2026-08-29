import importlib.util
from pathlib import Path

import pytest

SLOW_NAME_MARKERS = ("bruteforce", "brute_force", "exhaustive")


def pytest_collection_modifyitems(items):
    slow = pytest.mark.slow
    for item in items:
        name = item.name.lower()
        if any(marker in name for marker in SLOW_NAME_MARKERS):
            item.add_marker(slow)


@pytest.fixture
def solution(request):
    test_file = Path(str(request.node.path)).resolve()
    stem = test_file.stem
    assert stem.startswith("test_")

    date_code = stem.removeprefix("test_")
    assert len(date_code) == 8 and date_code.isdigit()

    root = Path(__file__).resolve().parents[1]
    path = root / "solutions" / date_code[:4] / date_code[:6] / f"{date_code}.py"

    spec = importlib.util.spec_from_file_location(f"daily_{date_code}", path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)

    return module.Solution()
