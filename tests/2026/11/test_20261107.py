def test_assign_tasks_examples(solution):
    # Official Example 1
    assert solution.assignTasks([3, 3, 2], [1, 2, 3, 2, 1, 2]) == [2, 2, 0, 2, 1, 2]

    # Official Example 2
    assert solution.assignTasks([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1]) == [
        1,
        4,
        1,
        4,
        1,
        3,
        2,
    ]

    # Trivial single-server identity case (expected output follows directly from spec)
    assert solution.assignTasks([1], [5]) == [0]
