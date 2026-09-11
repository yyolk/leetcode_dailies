# https://leetcode.com/problems/unique-3-digit-even-numbers/


class Solution:
    """3483. Unique 3-Digit Even Numbers

    You are given an array of digits called `digits`. Your task is to determine the
    number of **distinct** three-digit even numbers that can be formed using these
    digits.

    **Note**: Each *copy* of a digit can only be used **once per number**, and there may
    **not** be leading zeros.

    Constraints:

    * `3 <= digits.length <= 10`

    * `0 <= digits[i] <= 9`
    """

    def total_numbers(self, digits: list[int]) -> int:
        # Frequency count of each digit 0-9
        freq = [0] * 10
        for d in digits:
            freq[d] += 1

        count = 0
        # Hundreds place: cannot be 0
        for h in range(1, 10):
            if freq[h] == 0:
                continue
            freq[h] -= 1
            # Tens place: any remaining digit
            for t in range(10):
                if freq[t] == 0:
                    continue
                freq[t] -= 1
                # Units place: must be even
                for u in (0, 2, 4, 6, 8):
                    if freq[u] > 0:
                        count += 1
                freq[t] += 1
            freq[h] += 1

        return count

    totalNumbers = total_numbers
