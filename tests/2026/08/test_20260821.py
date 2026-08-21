from itertools import combinations


def brute_find_kth_smallest(coins: list[int], k: int) -> int:
    value = 0
    found = 0
    while found < k:
        value += 1
        if any(value % coin == 0 for coin in coins):
            found += 1
    return value


def test_find_kth_smallest_examples(solution):
    assert solution.findKthSmallest([3, 6, 9], 3) == 9
    assert solution.findKthSmallest([5, 2], 7) == 12
    assert solution.findKthSmallest([3, 6], 4) == 12


def test_find_kth_smallest_matches_bruteforce(solution):
    for size in range(1, 5):
        for coins in combinations(range(1, 8), size):
            coins_list = list(coins)
            for k in range(1, 41):
                expected = brute_find_kth_smallest(coins_list, k)
                actual = solution.findKthSmallest(coins_list, k)
                assert actual == expected, (coins_list, k, expected, actual)


def test_find_kth_smallest_large_k_with_coin_one(solution):
    assert solution.findKthSmallest([1, 7, 11], 2_000_000_000) == 2_000_000_000
