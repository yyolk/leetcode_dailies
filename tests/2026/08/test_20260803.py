def test_stone_game_iii_examples(solution):
    assert solution.stoneGameIII([1, 2, 3, 7]) == "Bob"
    assert solution.stoneGameIII([1, 2, 3, -9]) == "Alice"
    assert solution.stoneGameIII([1, 2, 3, 6]) == "Tie"
