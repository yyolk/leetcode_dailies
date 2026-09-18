def test_max_num_of_substrings_examples(solution):
    # Example 1
    assert sorted(solution.maxNumOfSubstrings("adefaddaccc")) == sorted(
        ["e", "f", "ccc"]
    )

    # Example 2
    assert sorted(solution.maxNumOfSubstrings("abbaccd")) == sorted(["d", "bb", "cc"])


def test_max_num_of_substrings_single_char(solution):
    # Whole string is the only valid substring.
    assert solution.maxNumOfSubstrings("a") == ["a"]
