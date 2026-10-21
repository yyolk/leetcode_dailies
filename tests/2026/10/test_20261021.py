def test_min_operations_examples(solution):
    # Official Example 1: s = "dog" -> 1
    assert solution.minOperations("dog") == 1

    # Official Example 2: s = "card" -> 2
    assert solution.minOperations("card") == 2

    # Official Example 3: s = "gf" -> -1
    assert solution.minOperations("gf") == -1


def test_min_operations_single(solution):
    # Single element is already sorted; expected output is 0 by the spec.
    assert solution.minOperations("a") == 0
