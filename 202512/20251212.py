# https://leetcode.com/problems/count-mentions-per-user
from bisect import bisect_left


class Solution:
    """3433. Count Mentions Per User

    You are given an integer numberOfUsers representing the total
    number of users and an array events of size n x 3.

    Each events[i] can be either of the following two types:

    Message Event: ["MESSAGE", "timestampi", "mentions_stringi"]
    This event indicates that a set of users was mentioned in a
    message at timestampi. The mentions_stringi string can contain
    one of the following tokens: id<number>: where <number> is an
    integer in range [0,numberOfUsers - 1]. There can be multiple
    ids separated by a single whitespace and may contain
    duplicates. This can mention even the offline users. ALL:
    mentions all users. HERE: mentions all online users.

    Offline Event: ["OFFLINE", "timestampi", "idi"]
    This event indicates that the user idi had become offline at
    timestampi for 60 time units. The user will automatically be
    online again at time timestampi + 60.

    Return an array mentions where mentions[i] represents the
    number of mentions the user with id i has across all MESSAGE
    events.

    All users are initially online, and if a user goes offline or
    comes back online, their status change is processed before
    handling any message event that occurs at the same timestamp.

    Note that a user can be mentioned multiple times in a single
    message event, and each mention should be counted separately.
    """
    def count_mentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        # Collect specific mentions, ALL counts, HERE events, and offline starts
        specific = [0] * numberOfUsers
        total_all = 0
        here_events = []  # (timestamp, h_count)
        offline_starts = [[] for _ in range(numberOfUsers)]
        
        for event in events:
            event_type = event[0]
            if event_type == "MESSAGE":
                t = int(event[1])
                tokens = event[2].split()
                h_count = 0
                for token in tokens:
                    if token == "ALL":
                        total_all += 1
                    elif token == "HERE":
                        h_count += 1
                    elif token.startswith("id"):
                        try:
                            uid = int(token[2:])
                            if 0 <= uid < numberOfUsers:
                                specific[uid] += 1
                        except ValueError:
                            pass  # Invalid token
                if h_count > 0:
                    here_events.append((t, h_count))
            elif event_type == "OFFLINE":
                t = int(event[1])
                uid = int(event[2])
                if 0 <= uid < numberOfUsers:
                    offline_starts[uid].append(t)
        
        # Compute total HERE mentions if always online
        total_here = sum(h for _, h in here_events)
        
        # Sort HERE events by timestamp
        here_events.sort(key=lambda x: x[0])
        times = [t for t, _ in here_events]
        # Prefix sums for quick range queries
        prefix = [0] * (len(here_events) + 1)
        for i in range(len(here_events)):
            prefix[i + 1] = prefix[i] + here_events[i][1]
        
        # Initialize mentions with specific + ALL + full HERE
        mentions = [specific[i] + total_all + total_here for i in range(numberOfUsers)]
        
        # For each user, compute missed HERE due to offline periods
        for i in range(numberOfUsers):
            starts = offline_starts[i]
            if not starts:
                continue
            # Sort starts and merge overlapping offline intervals [s, s+60)
            starts.sort()
            intervals = []
            curr_start = starts[0]
            curr_end = starts[0] + 60
            for s in starts[1:]:
                if s < curr_end:
                    curr_end = max(curr_end, s + 60)
                else:
                    intervals.append((curr_start, curr_end))
                    curr_start = s
                    curr_end = s + 60
            intervals.append((curr_start, curr_end))
            
            # For each merged offline interval [l, r), sum h for HERE t in [l, r)
            missed = 0
            for l, r in intervals:
                # Binary search for first t >= l
                left_idx = bisect_left(times, l)
                # Binary search for first t >= r
                right_idx = bisect_left(times, r)
                missed += prefix[right_idx] - prefix[left_idx]
            
            mentions[i] -= missed
        
        return mentions

    countMentions = count_mentions