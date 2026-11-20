def test_max_selected_elements_examples(solution):
    # Official Example 1.
    assert solution.maxSelectedElements([2, 1, 5, 1, 1]) == 3

    # Official Example 2.
    assert solution.maxSelectedElements([1, 4, 7, 10]) == 1

    # Trivial single-element case (obvious from spec).
    assert solution.maxSelectedElements([5]) == 1
