def test_palindrome_path_examples(solution):
    # Official Example 1.
    n1 = 3
    edges1 = [[0, 1], [1, 2]]
    s1 = "aac"
    queries1 = ["query 0 2", "update 1 b", "query 0 2"]
    assert solution.palindromePath(n1, edges1, s1, queries1) == [True, False]

    # Official Example 2.
    n2 = 4
    edges2 = [[0, 1], [0, 2], [0, 3]]
    s2 = "abca"
    queries2 = [
        "query 1 2",
        "update 0 b",
        "query 2 3",
        "update 3 a",
        "query 1 3",
    ]
    assert solution.palindromePath(n2, edges2, s2, queries2) == [False, False, True]

    # Trivial single-node identity case.
    assert solution.palindromePath(1, [], "a", ["query 0 0"]) == [True]
