# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    """2657. Find the Prefix Common Array of Two Arrays
    
    You are given two 0-indexed integer permutations A and B of length n.
    A prefix common array of A and B is an array C such that C[i] is equal to the
    count of numbers that are present at or before the index i in both A and B.
    Return the prefix common array of A and B.
    A sequence of n integers is called a permutation if it contains all integers from
    1 to n exactly once.
    """
    def find_the_prefix_common_array(self, a: list[int], b: list[int]) -> list[int]:
        n = len(a)
        # seen tracks occurrences in the two prefixes combined
        seen = [0] * (n + 1)
        count = 0
        result = [0] * n
        for i in range(n):
            # process A[i]
            seen[a[i]] += 1
            if seen[a[i]] == 2:
                count += 1
            # process B[i]
            seen[b[i]] += 1
            if seen[b[i]] == 2:
                count += 1
            result[i] = count
        return result

    findThePrefixCommonArray = find_the_prefix_common_array