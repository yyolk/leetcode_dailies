# https://leetcode.com/problems/student-attendance-record-ii/
MOD = 10**9 + 7


class Solution:
    """552. Student Attendance Record II

    An attendance record for a student can be represented as a string where each
    character signifies whether the student was absent, late, or present on that day.
    The record only contains the following three characters:

    * `'A'`: Absent.

    * `'L'`: Late.

    * `'P'`: Present.

    Any student is eligible for an attendance award if they meet **both** of the
    following criteria:

    * The student was absent (`'A'`) for **strictly** fewer than 2 days **total**.

    * The student was **never** late (`'L'`) for 3 or more **consecutive** days.

    Given an integer `n`, return *the **number** of possible attendance records of
    length* `n` *that make a student eligible for an attendance award. The answer may be
    very large, so return it **modulo*** `109 + 7`.

    """

    def check_record(self, n: int) -> int:
        # Initialize DP array
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1  # Base case: an empty sequence

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Add 'P' to the sequence
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    # Add 'A' to the sequence
                    if j > 0:
                        dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j - 1][k]) % MOD

                    # Add 'L' to the sequence
                    if k > 0:
                        dp[i][j][k] = (dp[i][j][k] + dp[i - 1][j][k - 1]) % MOD

        # Sum up all valid sequences of length n
        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD

        return result

    checkRecord = check_record
