# https://leetcode.com/problems/minimum-penalty-for-a-shop


class Solution:
    """2483. Minimum Penalty for a Shop

    Given a string customers of 'Y' (customer present) and 'N' (no customer),
    find the earliest closing hour (0 to n inclusive) that minimizes the
    penalty. Penalty is the number of hours the shop is open with no
    customers plus the number of hours it is closed with customers present.
    """
    def best_closing_time(self, customers: str) -> int:
        n = len(customers)
        
        # Precompute prefix sum: number of 'Y's up to index i (customers[0..i])
        prefix_y = [0] * (n + 1)
        for i in range(n):
            prefix_y[i + 1] = prefix_y[i] + (1 if customers[i] == 'Y' else 0)
        
        min_penalty = float('inf')
        best_hour = 0
        
        # Try every possible closing hour j (shop open during 0..j-1, closed at j..n-1)
        for j in range(n + 1):
            # Hours open with no customers: total 'N's before j
            open_no_cust = j - prefix_y[j]
            
            # Hours closed with customers: total 'Y's from j onward
            closed_with_cust = prefix_y[n] - prefix_y[j]
            
            penalty = open_no_cust + closed_with_cust
            
            # Update if better; use <= to prefer earliest hour on tie
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j
        
        return best_hour

    bestClosingTime = best_closing_time