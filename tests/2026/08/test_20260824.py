from functools import lru_cache


def brute_stone_game_viii(stones: list[int]) -> int:
    @lru_cache(maxsize=None)
    def solve(state: tuple[int, ...]) -> int:
        if len(state) <= 1:
            return 0

        prefix = state[0]
        best = -10**18
        for x in range(2, len(state) + 1):
            prefix += state[x - 1]
            next_state = (prefix,) + state[x:]
            best = max(best, prefix - solve(next_state))
        return best

    return solve(tuple(stones))


def test_stone_game_viii_examples(solution):
    assert solution.stoneGameVIII([-1, 2, -3, 4, -5]) == 5
    assert solution.stoneGameVIII([7, -6, 5, 10, 5, -2, -6]) == 13
    assert solution.stoneGameVIII([-10, -12]) == -22


def test_stone_game_viii_matches_bruteforce(solution):
    values = (-2, -1, 0, 1, 2)
    for n in range(2, 7):
        total = len(values) ** n
        for mask in range(total):
            arr = [0] * n
            tmp = mask
            for i in range(n):
                arr[i] = values[tmp % len(values)]
                tmp //= len(values)
            expected = brute_stone_game_viii(arr)
            actual = solution.stoneGameVIII(arr)
            assert actual == expected, (arr, expected, actual)
