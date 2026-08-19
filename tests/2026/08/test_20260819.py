from itertools import product


def brute_max_number_of_families(n: int, reserved_seats: list[list[int]]) -> int:
    reserved_by_row: dict[int, set[int]] = {}
    for row, seat in reserved_seats:
        reserved_by_row.setdefault(row, set()).add(seat)

    blocks = ((2, 3, 4, 5), (4, 5, 6, 7), (6, 7, 8, 9))

    total = 0
    for row in range(1, n + 1):
        reserved = reserved_by_row.get(row, set())
        best = 0
        for use_mask in range(1 << len(blocks)):
            used_seats: set[int] = set()
            valid = True
            count = 0
            for idx, block in enumerate(blocks):
                if (use_mask >> idx) & 1:
                    if any(seat in reserved or seat in used_seats for seat in block):
                        valid = False
                        break
                    used_seats.update(block)
                    count += 1
            if valid:
                best = max(best, count)
        total += best
    return total


def test_max_number_of_families_examples(solution):
    assert (
        solution.maxNumberOfFamilies(
            3,
            [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]],
        )
        == 4
    )
    assert solution.maxNumberOfFamilies(2, [[2, 1], [1, 8], [2, 6]]) == 2
    assert solution.maxNumberOfFamilies(4, [[4, 3], [1, 4], [4, 6], [1, 7]]) == 4


def test_max_number_of_families_single_row_exhaustive(solution):
    for row_mask in range(1 << 10):
        reserved_seats = [[1, seat + 1] for seat in range(10) if (row_mask >> seat) & 1]
        expected = brute_max_number_of_families(1, reserved_seats)
        actual = solution.maxNumberOfFamilies(1, reserved_seats)
        assert actual == expected, (row_mask, expected, actual)


def test_max_number_of_families_multi_row_samples(solution):
    sample_masks = (
        0,
        0b0000000001,
        0b1000000000,
        0b0000011110,
        0b0111100000,
        0b0011110000,
        0b1111111111,
    )

    for n in range(1, 4):
        for masks in product(sample_masks, repeat=n):
            reserved_seats: list[list[int]] = []
            for row, row_mask in enumerate(masks, start=1):
                for seat in range(10):
                    if (row_mask >> seat) & 1:
                        reserved_seats.append([row, seat + 1])

            expected = brute_max_number_of_families(n, reserved_seats)
            actual = solution.maxNumberOfFamilies(n, reserved_seats)
            assert actual == expected, (n, masks, expected, actual)


def test_max_number_of_families_large_n_sparse_rows(solution):
    n = 10**9
    reserved_seats = [[1, 2]]
    assert solution.maxNumberOfFamilies(n, reserved_seats) == 2 * n - 1
