def brute_check_divisibility(n: int) -> bool:
    digit_sum = sum(int(ch) for ch in str(n))
    digit_product = 1
    for ch in str(n):
        digit_product *= int(ch)
    return n % (digit_sum + digit_product) == 0


def test_check_divisibility_examples(solution):
    assert solution.checkDivisibility(99) is True
    assert solution.checkDivisibility(23) is False


def test_check_divisibility_matches_bruteforce(solution):
    for n in range(1, 10_001):
        expected = brute_check_divisibility(n)
        actual = solution.checkDivisibility(n)
        assert actual == expected, (n, expected, actual)
