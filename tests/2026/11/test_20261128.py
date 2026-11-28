def test_maximum_sale_items_examples(solution):
    # Official Example 1
    assert solution.maximumSaleItems([[1, 6], [2, 4], [3, 5]], 19) == 5
    # Official Example 2
    assert (
        solution.maximumSaleItems(
            [[2, 8], [1, 10], [6, 6], [4, 12], [5, 20], [5, 17]], 35
        )
        == 7
    )
