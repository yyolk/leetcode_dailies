# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/


class Solution:
    """2138. Divide a String Into Groups of Size k

    A string `s` can be partitioned into groups of size `k` using the following
    procedure:

    * The first group consists of the first `k` characters of the string, the second
    group consists of the next `k` characters of the string, and so on. Each element can
    be a part of **exactly one** group.

    * For the last group, if the string **does not** have `k` characters remaining, a
    character `fill` is used to complete the group.

    Note that the partition is done so that after removing the `fill` character from the
    last group (if it exists) and concatenating all the groups in order, the resultant
    string should be `s`.

    Given the string `s`, the size of each group `k` and the character `fill`, return *a
    string array denoting the **composition of every group*** `s` *has been divided
    into, using the above procedure*."""

    def divide_string(self, s: str, k: int, fill: str) -> list[str]:
        # Create list of groups using list comprehension
        result = [s[i : i + k] for i in range(0, len(s), k)]
        # Check and fill the last group if necessary
        if result and len(result[-1]) < k:
            result[-1] += fill * (k - len(result[-1]))
        return result

    divideString = divide_string
