# https://leetcode.com/problems/champagne-tower


class Solution:
    """799. Champagne Tower
    
    We stack glasses in a pyramid, where the first row has 1 glass, the
    second row has 2 glasses, and so on until the 100th row. Each glass
    holds one cup of champagne.
    
    Then, some champagne is poured into the first glass at the top. When
    the topmost glass is full, any excess liquid poured will fall equally
    to the glass immediately to the left and right of it. When those
    glasses become full, any excess champagne will fall equally to the
    left and right of those glasses, and so on. (A glass at the bottom row
    has its excess champagne fall on the floor.)
    
    Given integers poured, query_row, and query_glass (0-indexed), return
    how much champagne is in the glass at query_row, query_glass.
    """

    def champagne_tower(self, poured: int, query_row: int, query_glass: int) -> float:
        # Start with all poured champagne in the top glass
        current_row = [float(poured)]

        # Simulate flow down to the query row
        for _ in range(query_row):
            # Next row has one more glass than current
            next_row = [0.0] * (len(current_row) + 1)

            for j, amount in enumerate(current_row):
                # Overflow from current glass (0 if <= 1)
                overflow = max(amount - 1.0, 0.0) / 2.0
                # Distribute equally to left and right glasses below
                next_row[j] += overflow
                next_row[j + 1] += overflow

            current_row = next_row

        # Amount in the queried glass, capped at full (1.0)
        return min(1.0, current_row[query_glass])

    champagneTower = champagne_tower