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
    ) -> int:
        # Determine number of users
        m = len(languages)
        # Convert languages to sets for efficient intersection checks
        lang_sets = [set(langs) for langs in languages]
        # Collect users involved in friendships where no common language exists
        affected_users = set()
        for u, v in friendships:
            u_idx = u - 1
            v_idx = v - 1
            # Check if the pair shares any language
            if not lang_sets[u_idx] & lang_sets[v_idx]:
                affected_users.add(u_idx)
                affected_users.add(v_idx)
        # If no affected users, no teaching needed
        if not affected_users:
            return 0
        # Initialize counts of how many affected users know each language
        know_counts = [0] * (n + 1)
        for user in affected_users:
            for lang in lang_sets[user]:
                know_counts[lang] += 1
        # The minimum teachings is total affected minus max already known for any language
        return len(affected_users) - max(know_counts)

    minimumTeachings = minimum_teachings
