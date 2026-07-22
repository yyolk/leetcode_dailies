# https://leetcode.com/problems/maximize-active-section-with-trade-ii/


class Solution:
    """3501. Maximize Active Section with Trade II

    You are given a binary string `s` of length `n`, where:
    * `'1'` represents an **active** section.
    * `'0'` represents an **inactive** section.
    You can perform **at most one trade** to maximize the number of active
    sections in `s`. In a trade, you:
    * Convert a contiguous block of `'1'`s that is surrounded by `'0'`s to all
      `'0'`s.
    * Afterward, convert a contiguous block of `'0'`s that is surrounded by
      `'1'`s to all `'1'`s.
    Additionally, you are given a **2D array** `queries`, where
    `queries[i] = [li, ri]` represents a substring `s[li...ri]`.
    For each query, determine the **maximum** possible number of active
    sections in `s` after making the optimal trade on the substring
    `s[li...ri]`.
    Return an array `answer`, where `answer[i]` is the result for
    `queries[i]`.
    **Note**
    * For each query, treat `s[li...ri]` as if it is **augmented** with a
      `'1'` at both ends, forming `t = '1' + s[li...ri] + '1'`. The
      augmented `'1'`s **do not** contribute to the final count.
    * The queries are independent of each other.
    Constraints:
    * `1 <= n == s.length <= 105`
    * `1 <= queries.length <= 105`
    * `s[i]` is either `'0'` or `'1'`.
    * `queries[i] = [li, ri]`
    * `0 <= li <= ri < n`
    """

    def max_active_sections_after_trade(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        ones = s.count("1")
        # zero_groups: list of [start, length] for each contiguous 0-run
        # zero_group_index[i]: index of last 0-group at or before i (-1 if none)
        zero_groups, zero_group_index = self._get_zero_groups(s)
        if not zero_groups:
            return [ones] * len(queries)

        # merge_lengths[k] = length of zero-group k + length of zero-group k+1
        merge_lengths = self._get_zero_merge_lengths(zero_groups)
        st = self._SparseTable(merge_lengths)

        ans = []
        for l, r in queries:
            # partial zeros from l to end of its group (or -1)
            left = (
                -1
                if zero_group_index[l] == -1
                else zero_groups[zero_group_index[l]][1]
                - (l - zero_groups[zero_group_index[l]][0])
            )
            # partial zeros from start of its group to r (or -1)
            right = (
                -1
                if zero_group_index[r] == -1
                else r - zero_groups[zero_group_index[r]][0] + 1
            )

            # range of fully-covered zero groups inside [l, r]
            start_g = zero_group_index[l] + 1
            end_g = zero_group_index[r] if s[r] == "1" else zero_group_index[r] - 1
            # corresponding indices into the merge_lengths array
            start_m, end_m = start_g, end_g - 1

            active = ones
            # special: l and r lie in two consecutive zero-groups
            # (the single intervening 1-group is fully inside)
            if (
                s[l] == "0"
                and s[r] == "0"
                and zero_group_index[l] + 1 == zero_group_index[r]
            ):
                active = max(active, ones + left + right)
            # max over any fully-covered adjacent pair of zero-groups
            elif start_m <= end_m:
                active = max(active, ones + st.query(start_m, end_m))

            # left partial + the next full zero-group
            end_check = zero_group_index[r] if s[r] == "1" else zero_group_index[r] - 1
            if s[l] == "0" and zero_group_index[l] + 1 <= end_check:
                active = max(
                    active,
                    ones + left + zero_groups[zero_group_index[l] + 1][1],
                )
            # previous full zero-group + right partial
            if s[r] == "0" and zero_group_index[l] < zero_group_index[r] - 1:
                active = max(
                    active,
                    ones + right + zero_groups[zero_group_index[r] - 1][1],
                )
            ans.append(active)
        return ans

    def _get_zero_groups(self, s: str) -> tuple[list[list[int]], list[int]]:
        zero_groups: list[list[int]] = []
        zero_group_index: list[int] = []
        for i, c in enumerate(s):
            if c == "0":
                if i > 0 and s[i - 1] == "0":
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
                zero_group_index.append(len(zero_groups) - 1)
            else:
                # still record the most recent zero-group index
                zero_group_index.append(len(zero_groups) - 1)
        return zero_groups, zero_group_index

    def _get_zero_merge_lengths(self, zero_groups: list[list[int]]) -> list[int]:
        return [
            zero_groups[i][1] + zero_groups[i + 1][1]
            for i in range(len(zero_groups) - 1)
        ]

    class _SparseTable:
        def __init__(self, nums: list[int]):
            self.n = len(nums)
            if self.n == 0:
                self.st: list[list[int]] = []
                return
            bits = self.n.bit_length()
            self.st = [[0] * self.n for _ in range(bits + 1)]
            self.st[0] = nums[:]
            for i in range(1, bits + 1):
                step = 1 << (i - 1)
                for j in range(self.n - (1 << i) + 1):
                    self.st[i][j] = max(self.st[i - 1][j], self.st[i - 1][j + step])

        def query(self, l: int, r: int) -> int:
            if l > r or self.n == 0:
                return 0
            i = (r - l + 1).bit_length() - 1
            return max(self.st[i][l], self.st[i][r - (1 << i) + 1])

    maxActiveSectionsAfterTrade = max_active_sections_after_trade
