from functools import lru_cache


@lru_cache(maxsize=None)
def _bruteforce_alice_wins(state: str, alice_turn: bool) -> bool:
    if "?" not in state:
        half = len(state) // 2
        left = sum(int(ch) for ch in state[:half])
        right = sum(int(ch) for ch in state[half:])
        return left != right

    idx = state.index("?")
    outcomes = (
        _bruteforce_alice_wins(
            state[:idx] + str(digit) + state[idx + 1 :], not alice_turn
        )
        for digit in range(10)
    )
    return any(outcomes) if alice_turn else all(outcomes)


def test_sum_game_examples(solution):
    assert solution.sumGame("5023") is False
    assert solution.sumGame("25??") is True
    assert solution.sumGame("?3295???") is False


def test_sum_game_matches_bruteforce_on_small_states(solution):
    chars = "01?"
    for a in chars:
        for b in chars:
            for c in chars:
                for d in chars:
                    num = a + b + c + d
                    expected = _bruteforce_alice_wins(num, True)
                    actual = solution.sumGame(num)
                    assert actual == expected, (num, expected, actual)
