def brute_shortest_beautiful_substring(s: str, k: int) -> str:
    best = ""
    best_len = len(s) + 1
    for i in range(len(s)):
        ones = 0
        for j in range(i, len(s)):
            if s[j] == "1":
                ones += 1
            if ones == k:
                candidate = s[i : j + 1]
                candidate_len = j - i + 1
                if candidate_len < best_len or (
                    candidate_len == best_len and candidate < best
                ):
                    best = candidate
                    best_len = candidate_len
    return best


def test_shortest_beautiful_substring_examples(solution):
    assert solution.shortestBeautifulSubstring("100011001", 3) == "11001"
    assert solution.shortestBeautifulSubstring("1011", 2) == "11"
    assert solution.shortestBeautifulSubstring("000", 1) == ""


def test_shortest_beautiful_substring_matches_bruteforce(solution):
    for n in range(1, 8):
        for mask in range(1 << n):
            bits = "".join("1" if mask & (1 << i) else "0" for i in range(n))
            for k in range(1, n + 1):
                expected = brute_shortest_beautiful_substring(bits, k)
                actual = solution.shortestBeautifulSubstring(bits, k)
                assert actual == expected, (bits, k, expected, actual)
