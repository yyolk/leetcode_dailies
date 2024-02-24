# https://leetcode.com/problems/find-all-people-with-secret/


class Solution:
    """2092. Find All People With Secret

    You are given an integer `n` indicating there are `n` people numbered from `0` to `n
    - 1`. You are also given a **0-indexed** 2D integer array `meetings` where
    `meetings[i] = [xi, yi, timei]` indicates that person `xi` and person `yi` have a
    meeting at `timei`. A person may attend **multiple meetings** at the same time.
    Finally, you are given an integer `first_person`.

    Person `0` has a **secret** and initially shares the secret with a person
    `first_person` at time `0`. This secret is then shared every time a meeting takes
    place with a person that has the secret. More formally, for every meeting, if a
    person `xi` has the secret at `timei`, then they will share the secret with person
    `yi`, and vice versa.

    The secrets are shared **instantaneously**. That is, a person may receive the secret
    and share it with people in other meetings within the same time frame.

    Return *a list of all the people that have the secret after all the meetings have
    taken place.* You may return the answer in **any order**.

    """

    def find_all_people(
        self, n: int, meetings: list[list[int]], first_person: int
    ) -> list[int]: ...

    findAllPeople = find_all_people
