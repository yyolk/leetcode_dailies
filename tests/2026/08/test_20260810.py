from functools import lru_cache


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


def test_stone_game_iv_examples(solution):
    assert solution.winnerSquareGame(1) is True
    assert solution.winnerSquareGame(2) is False
    assert solution.winnerSquareGame(4) is True


def test_stone_game_iv_matches_bruteforce_small_inputs(solution):
    for n in range(1, 201):
        expected = brute_winner_square_game(n)
        actual = solution.winnerSquareGame(n)
        assert actual is expected, (n, expected, actual)
