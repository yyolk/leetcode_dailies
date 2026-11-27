def test_maximum_sale_items_examples(solution):
    # Example 1
    assert solution.maximumSaleItems([[6, 2], [2, 6], [3, 4]], 9) == 4

    # Example 2
    assert solution.maximumSaleItems(
        [[2, 4], [3, 2], [4, 1], [6, 4], [12, 4]], 8
    ) == 10
