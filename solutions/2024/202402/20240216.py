# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/


class Solution:
    """1481. Least Number of Unique Integers after K Removals

    Given an array of integers `arr` and an integer `k`. Find the *least number of
    unique integers* after removing **exactly** `k` elements**.**

    """

    def find_least_num_of_unique_ints(self, arr: list[int], k: int) -> int:
        # Count the occurrences of each element in the array
        element_count = {}
        for num in arr:
            element_count[num] = element_count.get(num, 0) + 1

        # Sort the elements based on their occurrences
        sorted_elements = sorted(element_count.items(), key=lambda x: x[1])

        # Remove the least frequent elements until k becomes zero
        unique_count = len(sorted_elements)
        for _, count in sorted_elements:
            if k >= count:
                k -= count
                unique_count -= 1
            else:
                break

        return unique_count

    findLeastNumOfUniqueInts = find_least_num_of_unique_ints
