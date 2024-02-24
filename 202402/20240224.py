# https://leetcode.com/problems/find-all-people-with-secret/
from collections import deque


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
    ) -> list[int]:
        # Initialize the set with people who initially know the secret
        known_set = set([0, first_person])
        
        # Sort meetings by time
        sorted_meetings = []
        meetings.sort(key=lambda x: x[2])

        seen_time = set()

        # Group meetings by time
        for meeting in meetings:
            if meeting[2] not in seen_time:
                seen_time.add(meeting[2])
                sorted_meetings.append([])
            sorted_meetings[-1].append((meeting[0], meeting[1]))

        # Process meetings in sorted order
        for meeting_group in sorted_meetings:
            people_know_secret = set()
            graph = defaultdict(list)

            # Build graph and identify people who already know the secret
            for p1, p2 in meeting_group:
                graph[p1].append(p2)
                graph[p2].append(p1)
                if p1 in known_set:
                    people_know_secret.add(p1)
                if p2 in known_set:
                    people_know_secret.add(p2)

            # Use BFS to propagate the secret to connected people
            queue = deque(people_know_secret)

            while queue:
                curr = queue.popleft()
                known_set.add(curr)
                for neighbor in graph[curr]:
                    if neighbor not in known_set:
                        known_set.add(neighbor)
                        queue.append(neighbor)

        # Convert the final set to a list and return
        return list(known_set)

    findAllPeople = find_all_people
