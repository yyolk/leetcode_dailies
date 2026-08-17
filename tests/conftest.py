import importlib.util
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def solution(request):
    date = Path(str(request.fspath)).stem.removeprefix("test_")
    solution_path = ROOT / "solutions" / date[:4] / date[:6] / f"{date}.py"
    spec = importlib.util.spec_from_file_location(f"daily_{date}", solution_path)
    module = importlib.util.module_from_spec(spec)
    assert spec is not None and spec.loader is not None
    spec.loader.exec_module(module)
    return module.Solution()
