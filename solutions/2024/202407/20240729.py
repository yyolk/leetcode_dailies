# https://leetcode.com/problems/count-number-of-teams/


class Solution:
    """1395. Count Number of Teams

    There are `n` soldiers standing in a line. Each soldier is assigned a **unique**
    `rating` value.

    You have to form a team of 3 soldiers amongst them under the following rules:

    * Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`,
    `rating[j]`, `rating[k]`).

    * A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] >
    rating[j] > rating[k]`) where (`0 <= i < j < k < n`).

    Return the number of teams you can form given the conditions. (soldiers can be part
    of multiple teams).

    """

    def num_teams(self, rating: list[int]) -> int:
        # Initialize the count of valid teams to 0
        count = 0

        # Loop through each soldier, treating them as the middle soldier of the team
        for j in range(1, len(rating) - 1):
            # Initialize counters for soldiers less and greater than rating[j] on the left and right
            left_less = left_greater = right_less = right_greater = 0

            # Count soldiers on the left of j with ratings less than and greater than rating[j]
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1

            # Count soldiers on the right of j with ratings less than and greater than rating[j]
            for k in range(j + 1, len(rating)):
                if rating[k] < rating[j]:
                    right_less += 1
                elif rating[k] > rating[j]:
                    right_greater += 1

            # Calculate the number of valid increasing teams with j as the middle soldier
            count += left_less * right_greater

            # Calculate the number of valid decreasing teams with j as the middle soldier
            count += left_greater * right_less

        # Return the total number of valid teams
        return count

    numTeams = num_teams
