def brute(num: str, t: int, limit: int = 300000) -> str:
    start = int(num)
    target_len = len(num) + 3
    upper = min(limit, 10**target_len - 1)
    for value in range(start, upper + 1):
        s = str(value)
        if "0" in s:
            continue
        product = 1
        for ch in s:
            product *= int(ch)
        if product % t == 0:
            return s
    return "-1"


def test_smallest_divisible_digit_product_ii_known_cases(solution):
    assert solution.smallestNumber("1234", 256) == "1488"
    assert solution.smallestNumber("12355", 50) == "12355"
    assert solution.smallestNumber("11111", 26) == "-1"
    assert solution.smallestNumber("109", 2) == "112"
    assert solution.smallestNumber("99", 2) == "112"


def test_smallest_divisible_digit_product_ii_matches_bruteforce_small_inputs(solution):
    for number in range(11, 160):
        num = str(number)
        for t in range(1, 31):
            expected = brute(num, t)
            actual = solution.smallestNumber(num, t)
            assert actual == expected, (num, t, expected, actual)
