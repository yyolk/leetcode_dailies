# https://leetcode.com/problems/lemonade-change/


class Solution:
    """860. Lemonade Change

    At a lemonade stand, each lemonade costs `$5`. Customers are standing in a queue to
    buy from you and order one at a time (in the order specified by bills). Each
    customer will only buy one lemonade and pay with either a `$5`, `$10`, or `$20`
    bill. You must provide the correct change to each customer so that the net
    transaction is that the customer pays `$5`.

    Note that you do not have any change in hand at first.

    Given an integer array `bills` where `bills[i]` is the bill the `ith` customer pays,
    return `true` *if you can provide every customer with the correct change, or*
    `false` *otherwise*.

    """

    def lemonade_change(self, bills: list[int]) -> bool:
        # Initialize counters for $5 and $10 bills
        five_dollars = 0
        ten_dollars = 0

        # Iterate over each bill in the input list
        for bill in bills:
            if bill == 5:
                # If the customer pays with a $5 bill, increase $5 counter
                five_dollars += 1
            elif bill == 10:
                # If the customer pays with a $10 bill
                if five_dollars > 0:
                    # Give $5 as change, decrease $5 counter, and increase $10 counter
                    five_dollars -= 1
                    ten_dollars += 1
                else:
                    # If no $5 bill is available to give as change, return False
                    return False
            elif bill == 20:
                # If the customer pays with a $20 bill
                if ten_dollars > 0 and five_dollars > 0:
                    # Prefer to give one $10 and one $5 as change
                    ten_dollars -= 1
                    five_dollars -= 1
                elif five_dollars >= 3:
                    # If no $10 bill is available, give three $5 bills as change
                    five_dollars -= 3
                else:
                    # If neither combination is possible, return False
                    return False

        # If all customers received correct change, return True
        return True

    lemonadeChange = lemonade_change
