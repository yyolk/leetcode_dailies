# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/

class Solution:
    """1665. Minimum Initial Energy to Finish Tasks
    
    You are given an array tasks where tasks[i] = [actuali, minimumi]:
    actuali is the actual amount of energy you spend to finish the ith task.
    minimumi is the minimum amount of energy you require to begin the ith task.
    For example, if the task is [10, 12] and your current energy is 11, you
    cannot start this task. However, if your current energy is 13, you can
    complete this task, and your energy will be 3 after finishing it.
    You can finish the tasks in any order you like.
    Return the minimum initial amount of energy you will need to finish all
    the tasks.
    """
    def minimum_effort(self, tasks: list[list[int]]) -> int:
        ans = 0
        cur = 0
        # Sort by increasing (actual - minimum) i.e. descending (minimum - actual)
        # This order processes tasks with largest "startup overhead" first
        # to minimize cumulative peak energy required
        for actual, minimum in sorted(tasks, key=lambda x: x[0] - x[1]):
            if cur < minimum:
                # Add exactly the deficit to ans so this task can start
                # This accumulates the minimum initial energy needed
                ans += minimum - cur
                cur = minimum
            # Deduct actual cost after the task is started (cur now guaranteed
            # to be at least minimum before this subtraction)
            cur -= actual
        return ans

    minimumEffort = minimum_effort