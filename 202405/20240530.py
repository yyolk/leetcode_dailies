# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/


class Solution:
    """1442. Count Triplets That Can Form Two Arrays of Equal XOR

    Given an array of integers `arr`.

    We want to select three indices `i`, `j` and `k` where `(0 <= i < j <= k <
    arr.length)`.

    Let's define `a` and `b` as follows:

    * `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]`

    * `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]`

    Note that **^** denotes the **bitwise-xor** operation.

    Return *the number of triplets* (`i`, `j` and `k`) Where `a == b`.

    """

    def count_triplets(self, arr: list[int]) -> int:
        n = len(arr)
        prefix_xor = [0] * (n + 1)
        
        # Compute the prefix XOR array
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        count = 0
        
        # Iterate over each pair (i, k) to check the condition
        for i in range(n):
            for k in range(i + 1, n):
                if prefix_xor[i] == prefix_xor[k + 1]:
                    # For each valid (i, k), j can be any value between i+1 and k
                    count += k - i
        
        return count

    countTriplets = count_triplets
