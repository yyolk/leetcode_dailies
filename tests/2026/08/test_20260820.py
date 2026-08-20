from itertools import permutations


def brute_result_array(nums: list[int]) -> list[int]:
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for value in nums[2:]:
        if arr1[-1] > arr2[-1]:
            arr1.append(value)
        else:
            arr2.append(value)
    return arr1 + arr2


def test_result_array_examples(solution):
    assert solution.resultArray([2, 1, 3]) == [2, 3, 1]
    assert solution.resultArray([5, 4, 3, 8]) == [5, 3, 4, 8]


def test_result_array_matches_bruteforce(solution):
    for n in range(3, 8):
        for nums in permutations(range(1, n + 1)):
            nums_list = list(nums)
            expected = brute_result_array(nums_list)
            actual = solution.resultArray(nums_list)
            assert actual == expected, (nums_list, expected, actual)
