# https://leetcode.com/problems/maximum-average-pass-ratio/
import heapq


class Solution:
    """1792. Maximum Average Pass Ratio

    There is a school that has classes of students and each class will be having a final
    exam. You are given a 2D integer array `classes`, where `classes[i] = [passi,
    totali]`. You know beforehand that in the `ith` class, there are `totali` total
    students, but only `passi` number of students will pass the exam.

    You are also given an integer `extra_students`. There are another `extra_students`
    brilliant students that are **guaranteed** to pass the exam of any class they are
    assigned to. You want to assign each of the `extra_students` students to a class in
    a way that **maximizes** the **average** pass ratio across **all** the classes.

    The **pass ratio** of a class is equal to the number of students of the class that
    will pass the exam divided by the total number of students of the class. The
    **average pass ratio** is the sum of pass ratios of all the classes divided by the
    number of the classes.

    Return *the **maximum** possible average pass ratio after assigning the*
    `extra_students` *students.* Answers within `10-5` of the actual answer will be
    accepted."""

    def max_average_ratio(
        self, classes: list[list[int]], extra_students: int
    ) -> float:
        # Function to calculate the gain in pass ratio for adding a student to a class
        def calculate_pass_ratio_gain(current_passing_students, current_total_students):
            return (current_passing_students + 1) / (current_total_students + 1) - current_passing_students / current_total_students
        
        # Max-heap to store the gain, -gain because heapq is a min-heap by default
        priority_queue = []
        for passing_students, total_students in classes:
            gain_in_ratio = calculate_pass_ratio_gain(passing_students, total_students)
            heapq.heappush(priority_queue, (-gain_in_ratio, passing_students, total_students))
        
        # Distribute the extra students
        for _ in range(extra_students):
            # Pop the class with the maximum gain
            neg_gain, passing_students, total_students = heapq.heappop(priority_queue)
            # Add one student to this class
            passing_students += 1
            total_students += 1
            # Recalculate gain and push back into priority queue
            new_gain = calculate_pass_ratio_gain(passing_students, total_students)
            heapq.heappush(priority_queue, (-new_gain, passing_students, total_students))
        
        # Calculate the final average pass ratio
        sum_of_pass_ratios = 0
        for _, passing_students, total_students in priority_queue:
            sum_of_pass_ratios += passing_students / total_students
        
        return sum_of_pass_ratios / len(classes)

    maxAverageRatio = max_average_ratio
