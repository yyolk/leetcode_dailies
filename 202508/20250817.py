# https://leetcode.com/problems/new-21-game/


class Solution:
    """837. New 21 Game

    Alice plays the following game, loosely based on the card game **"21"**.

    Alice starts with `0` points and draws numbers while she has less than `k` points.
    During each draw, she gains an integer number of points randomly from the range `[1,
    max_pts]`, where `max_pts` is an integer. Each draw is independent and the outcomes
    have equal probabilities.

    Alice stops drawing numbers when she gets `k` **or more points**.

    Return the probability that Alice has `n` or fewer points.

    Answers within `10-5` of the actual answer are considered accepted."""

    def new21_game(self, n: int, k: int, max_pts: int) -> float:
        # Base cases: If k is 0, Alice hasn't started drawing, so probability is 1.
        # If n is large enough to cover all possible scores beyond k-1 + max_pts, probability is also 1.
        if k == 0 or n >= k - 1 + max_pts:
            return 1.0
        
        # Initialize a DP array where probabilities[i] represents the probability of reaching exactly score i.
        probabilities = [0.0] * (n + 1)
        probabilities[0] = 1.0  # Starting point: probability of being at 0 is 1.
        
        # current_window_sum tracks the sum of probabilities in the current sliding window of size max_pts.
        # total_probability accumulates the probability of scores from k to n (desired outcomes).
        current_window_sum, total_probability = 1.0, 0.0
        
        # Iterate through each possible score from 1 to n.
        for current_score in range(1, n + 1):
            # The probability of reaching current_score is the average of the probabilities
            # from the previous max_pts scores (uniform draw from 1 to max_pts).
            probabilities[current_score] = current_window_sum / max_pts
            
            # If we haven't reached the stopping point k yet, add this probability to the window
            # because we can continue drawing from here.
            if current_score < k:
                current_window_sum += probabilities[current_score]
            else:
                # Otherwise, we've reached or exceeded k, so accumulate this into the total probability.
                total_probability += probabilities[current_score]
            
            # Slide the window: if the window exceeds max_pts, remove the oldest probability.
            if current_score >= max_pts:
                current_window_sum -= probabilities[current_score - max_pts]
        
        # Return the accumulated probability of scores between k and n.
        return total_probability

    new21Game = new21_game
