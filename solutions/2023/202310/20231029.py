# https://leetcode.com/problems/poor-pigs/
import math


class Solution:
    """458. Poor Pigs

    There are `buckets` buckets of liquid, where **exactly one** of the buckets is
    poisonous. To figure out which one is poisonous, you feed some number of (poor) pigs
    the liquid to see whether they will die or not. Unfortunately, you only have
    `minutes_to_test` minutes to determine which bucket is poisonous.

    You can feed the pigs according to these steps:

    1. Choose some live pigs to feed.

    2. For each pig, choose which buckets to feed it. The pig will consume all the
    chosen buckets simultaneously and will take no time. Each pig can feed from any
    number of buckets, and each bucket can be fed from by any number of pigs.

    3. Wait for `minutes_to_die` minutes. You may **not** feed any other pigs during
    this time.

    4. After `minutes_to_die` minutes have passed, any pigs that have been fed the
    poisonous bucket will die, and all others will survive.

    5. Repeat this process until you run out of time.

    Given `buckets`, `minutes_to_die`, and `minutes_to_test`, return *the **minimum**
    number of pigs needed to figure out which bucket is poisonous within the allotted
    time*.
    """

    def poor_pigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        """The minimum number of pigs needed to figure out which bucket is poisonous.

        Proposed solution using a binary search.

        Args:
            buckets (int): The number of buckets, of which one is poisonous.
            minutes_to_die (int): The number of minutes you may not feed any other pigs.
            minutes_to_test (int): The number of minutes you are allowed to test.

        Returns:
            int: The minimum number of pigs necesssary to figure out which bucket is
                poisonous.
        """
        return math.ceil(
            round(math.log(buckets) / math.log(minutes_to_test / minutes_to_die + 1), 2)
        )

    poorPigs = poor_pigs
