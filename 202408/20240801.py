# https://leetcode.com/problems/number-of-senior-citizens/


class Solution:
    """2678. Number of Senior Citizens

    You are given a **0\\-indexed** array of strings `details`. Each element of `details`
    provides information about a given passenger compressed into a string of length
    `15`. The system is such that:

    * The first ten characters consist of the phone number of passengers.

    * The next character denotes the gender of the person.

    * The following two characters are used to indicate the age of the person.

    * The last two characters determine the seat allotted to that person.

    Return *the number of passengers who are **strictly** **more than 60 years old**.*

    """

    def count_seniors(self, details: list[str]) -> int:
        count = 0
        for detail in details:
            # Extract the age from the 12th and 13th characters and convert it to an integer
            age = int(detail[11:13])
            # Check if the age is strictly greater than 60
            if age > 60:
                count += 1
        return count

    countSeniors = count_seniors
