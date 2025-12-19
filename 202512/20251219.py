# https://leetcode.com/problems/find-all-people-with-secret


class Solution:
    """2092. Find All People With Secret

    Person 0 shares the secret with firstPerson at time 0.
    Whenever two people meet at time t, if either knows the secret,
    both know it afterward (instantaneous sharing).
    Return all people who know the secret after all meetings.
    """
    def find_all_people(self, n: int, meetings: list[list[int]], firstPerson: int) -> list[int]:
        # Sort meetings by time (earliest first)
        meetings.sort(key=lambda x: x[2])
        
        # Union-Find with rank and path compression for efficiency
        parent = list(range(n))
        rank = [0] * n
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]
        
        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if rank[px] < rank[py]:
                    parent[px] = py
                elif rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[py] = px
                    rank[px] += 1
        
        # Person 0 and firstPerson start connected (know secret at time 0)
        union(0, firstPerson)
        
        i = 0
        m = len(meetings)
        while i < m:
            curr_time = meetings[i][2]
            connected = []  # people involved in meetings at curr_time
            
            # Process all meetings happening at the current time
            while i < m and meetings[i][2] == curr_time:
                x, y, _ = meetings[i]
                union(x, y)
                connected.extend([x, y])
                i += 1
            
            # After processing this time slot, keep only those connected to 0
            # Others met but neither knew the secret, so reset their parent
            root0 = find(0)
            connected = set(connected)  # unique people at this time
            for p in connected:
                if find(p) != root0:
                    parent[p] = p  # forget temporary unions (no secret)
        
        # Collect all people whose root is 0
        return [i for i in range(n) if find(i) == find(0)]

    findAllPeople = find_all_people