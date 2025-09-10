# https://leetcode.com/problems/minimum-number-of-people-to-teach/


class Solution:
    """1733. Minimum Number of People to Teach

    On a social network consisting of `m` users and some friendships between users, two
    users can communicate with each other if they know a common language.

    You are given an integer `n`, an array `languages`, and an array `friendships`
    where:

    * There are `n` languages numbered `1` through `n`,

    * `languages[i]` is the set of languages the `i\u200b\u200b\u200b\u200b\u200b\u200bth`\u200b\u200b\u200b\u200b user knows, and

    * `friendships[i] = [u\u200b\u200b\u200b\u200b\u200b\u200bi\u200b\u200b\u200b, v\u200b\u200b\u200b\u200b\u200b\u200bi]` denotes a friendship between the users
    `u\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200b\u200bi`\u200b\u200b\u200b\u200b\u200b and `vi`.

    You can choose **one** language and teach it to some users so that all friends can
    communicate with each other. Return *the* ***minimum*** *number of users you need to
    teach.*

    Note that friendships are not transitive, meaning if `x` is a friend of `y` and `y`
    is a friend of `z`, this doesn't guarantee that `x` is a friend of `z`."""

    def minimum_teachings(
        self, n: int, languages: list[list[int]], friendships: list[list[int]]
    ) -> int: ...

    minimumTeachings = minimum_teachings
