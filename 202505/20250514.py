# https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/
MOD = 1_000_000_007


class Solution:
    """3337. Total Characters in String After Transformations II

    You are given a string `s` consisting of lowercase English letters, an integer `t`
    representing the number of **transformations** to perform, and an array `nums` of
    size 26. In one **transformation**, every character in `s` is replaced according to
    the following rules:

    * Replace `s[i]` with the **next** `nums[s[i] - 'a']` consecutive characters in the
    alphabet. For example, if `s[i] = 'a'` and `nums[0] = 3`, the character `'a'`
    transforms into the next 3 consecutive characters ahead of it, which results in
    `"bcd"`.

    * The transformation **wraps** around the alphabet if it exceeds `'z'`. For example,
    if `s[i] = 'y'` and `nums[24] = 3`, the character `'y'` transforms into the next 3
    consecutive characters ahead of it, which results in `"zab"`.

    Return the length of the resulting string after **exactly** `t` transformations.

    Since the answer may be very large, return it **modulo** `10^9 + 7`."""

    def length_after_transformations(self, s: str, t: int, nums: list[int]) -> int:
        N = 26  # Size of alphabet (lowercase English letters)

        # Step 1: Build the transition matrix M
        # M[j][i] = 1 if character i transforms into character j
        M = [[0] * N for _ in range(N)]
        for i in range(N):
            for k in range(1, nums[i] + 1):
                j = (i + k) % N
                M[j][i] = 1

        # Step 2: Define matrix multiplication function
        def mat_mul(A, B):
            result = [[0] * N for _ in range(N)]
            for i in range(N):
                for j in range(N):
                    for k in range(N):
                        result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
            return result

        # Step 3: Define matrix exponentiation function using exponentiation by squaring
        def mat_pow(M, t):
            # Initialize result as identity matrix
            result = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
            while t > 0:
                if t % 2 == 1:
                    result = mat_mul(result, M)
                M = mat_mul(M, M)
                t //= 2
            return result

        # Step 4: Compute M^t
        M_t = mat_pow(M, t)

        # Step 5: Compute initial count vector from input string
        initial_count = [0] * N
        for char in s:
            idx = ord(char) - ord("a")
            initial_count[idx] += 1

        # Step 6: Compute final count vector: final_count = M_t * initial_count
        final_count = [0] * N
        for j in range(N):
            for i in range(N):
                final_count[j] = (final_count[j] + M_t[j][i] * initial_count[i]) % MOD

        # Step 7: Compute total length as sum of final_count modulo MOD
        total_length = sum(final_count) % MOD
        return total_length

    lengthAfterTransformations = length_after_transformations
