def test_max_palindromes_examples(solution):
    # Example 1: "aba" and "dbbd"
    assert solution.maxPalindromes("abaccdbbd", 3) == 2

    # Example 2: no palindrome of length at least 2
    assert solution.maxPalindromes("adbcda", 2) == 0


def test_max_palindromes_single_char_when_k_is_one(solution):
    # Every character is a palindrome of length 1.
    assert solution.maxPalindromes("abc", 1) == 3
