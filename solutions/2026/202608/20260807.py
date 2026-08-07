# https://leetcode.com/problems/smallest-divisible-digit-product-ii/


class Solution:
    """3348. Smallest Divisible Digit Product II

    You are given a string `num` which represents a **positive** integer, and an integer
    `t`.

    A number is called **zero-free** if *none* of its digits are 0.

    Return a string representing the **smallest** **zero-free** number greater than or
    equal to `num` such that the **product of its digits** is divisible by `t`. If no
    such number exists, return `"-1"`.

    Constraints:

    * `2 <= num.length <= 2 * 105`

    * `num` consists only of digits in the range `['0', '9']`.

    * `num` does not contain leading zeros.

    * `1 <= t <= 1014`"""

    def smallest_number(self, num: str, t: int) -> str:
        """Return the smallest zero-free number >= num with digit product divisible by t."""

        digit_factors = (
            (0, 0, 0, 0),  # 0 (unused in result)
            (0, 0, 0, 0),  # 1
            (1, 0, 0, 0),  # 2
            (0, 1, 0, 0),  # 3
            (2, 0, 0, 0),  # 4
            (0, 0, 1, 0),  # 5
            (1, 1, 0, 0),  # 6
            (0, 0, 0, 1),  # 7
            (3, 0, 0, 0),  # 8
            (0, 2, 0, 0),  # 9
        )

        need2 = need3 = need5 = need7 = 0
        for prime, ref in ((2, "need2"), (3, "need3"), (5, "need5"), (7, "need7")):
            while t % prime == 0:
                if ref == "need2":
                    need2 += 1
                elif ref == "need3":
                    need3 += 1
                elif ref == "need5":
                    need5 += 1
                else:
                    need7 += 1
                t //= prime
        if t != 1:
            return "-1"

        max2, max3 = need2, need3
        inf = 10**9
        dp23 = [[inf] * (max3 + 1) for _ in range(max2 + 1)]
        dp23[0][0] = 0
        moves23 = ((1, 0), (0, 1), (2, 0), (1, 1), (3, 0), (0, 2))
        for c2 in range(max2 + 1):
            for c3 in range(max3 + 1):
                cur = dp23[c2][c3]
                if cur == inf:
                    continue
                for a2, a3 in moves23:
                    n2 = min(max2, c2 + a2)
                    n3 = min(max3, c3 + a3)
                    if cur + 1 < dp23[n2][n3]:
                        dp23[n2][n3] = cur + 1

        def min_digits(r2: int, r3: int, r5: int, r7: int) -> int:
            return r5 + r7 + dp23[r2][r3]

        def build_smallest_suffix(
            length: int, r2: int, r3: int, r5: int, r7: int
        ) -> str:
            out = []
            for pos in range(length):
                slots_left = length - pos - 1
                for digit in range(1, 10):
                    d2, d3, d5, d7 = digit_factors[digit]
                    n2 = max(0, r2 - d2)
                    n3 = max(0, r3 - d3)
                    n5 = max(0, r5 - d5)
                    n7 = max(0, r7 - d7)
                    if min_digits(n2, n3, n5, n7) <= slots_left:
                        out.append(str(digit))
                        r2, r3, r5, r7 = n2, n3, n5, n7
                        break
            return "".join(out)

        n = len(num)
        prefix2 = [0] * (n + 1)
        prefix3 = [0] * (n + 1)
        prefix5 = [0] * (n + 1)
        prefix7 = [0] * (n + 1)
        prefix_zero = [0] * (n + 1)
        for i, ch in enumerate(num):
            digit = ord(ch) - ord("0")
            d2, d3, d5, d7 = digit_factors[digit]
            prefix2[i + 1] = prefix2[i] + d2
            prefix3[i + 1] = prefix3[i] + d3
            prefix5[i + 1] = prefix5[i] + d5
            prefix7[i + 1] = prefix7[i] + d7
            prefix_zero[i + 1] = prefix_zero[i] + (1 if digit == 0 else 0)

        if prefix_zero[n] == 0:
            if (
                prefix2[n] >= need2
                and prefix3[n] >= need3
                and prefix5[n] >= need5
                and prefix7[n] >= need7
            ):
                return num

        for i in range(n - 1, -1, -1):
            if prefix_zero[i] > 0:
                continue
            base2 = prefix2[i]
            base3 = prefix3[i]
            base5 = prefix5[i]
            base7 = prefix7[i]
            current_digit = ord(num[i]) - ord("0")
            for digit in range(max(1, current_digit + 1), 10):
                d2, d3, d5, d7 = digit_factors[digit]
                r2 = max(0, need2 - (base2 + d2))
                r3 = max(0, need3 - (base3 + d3))
                r5 = max(0, need5 - (base5 + d5))
                r7 = max(0, need7 - (base7 + d7))
                suffix_len = n - i - 1
                if min_digits(r2, r3, r5, r7) > suffix_len:
                    continue
                return (
                    num[:i]
                    + str(digit)
                    + build_smallest_suffix(suffix_len, r2, r3, r5, r7)
                )

        target_len = max(n + 1, min_digits(need2, need3, need5, need7))
        return build_smallest_suffix(target_len, need2, need3, need5, need7)

    smallestNumber = smallest_number
