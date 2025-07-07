# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/


class FindSumPairs:
    """1995. Finding Pairs With a Certain Sum

    You are given two integer arrays `nums1` and `nums2`. You are tasked to implement a
    data structure that supports queries of two types:

    1. **Add** a positive integer to an element of a given index in the array `nums2`.

    2. **Count** the number of pairs `(i, j)` such that `nums1[i] + nums2[j]` equals a
    given value (`0 <= i < nums1.length` and `0 <= j < nums2.length`).

    Implement the `FindSumPairs` class:

    * `FindSumPairs(int[] nums1, int[] nums2)` Initializes the `FindSumPairs` object
    with two integer arrays `nums1` and `nums2`.

    * `void add(int index, int val)` Adds `val` to `nums2[index]`, i.e., apply
    `nums2[index] += val`.

    * `int count(int tot)` Returns the number of pairs `(i, j)` such that `nums1[i] +
    nums2[j] == tot`."""

    def __init__(self, nums1: List[int], nums2: List[int]):
        """Initialize the FindSumPairs object with two integer arrays nums1 and nums2."""
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)  # Frequency map for nums2 elements

    def add(self, index: int, val: int) -> None:
        """Add val to nums2[index]."""
        old_val = self.nums2[index]
        self.nums2[index] += val
        new_val = self.nums2[index]
        self.freq[old_val] -= 1  # Decrease frequency of old value
        self.freq[new_val] += 1  # Increase frequency of new value

    def count(self, tot: int) -> int:
        """Return the number of pairs (i, j) such that nums1[i] + nums2[j] == tot."""
        result = 0
        for x in self.nums1:
            result += self.freq[tot - x]  # Add frequency of complement
        return result
