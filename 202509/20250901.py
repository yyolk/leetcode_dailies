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
        # Use a max-heap (simulated via min-heap with negative deltas) to prioritize classes by ratio increase
        heap = []
        # Initialize heap with classes where adding a student increases the ratio (pass < total)
        for i, (p, t) in enumerate(classes):
            if p < t:
                # Delta is the increase in pass ratio: (t - p) / (t * (t + 1))
                delta = (t - p) / (t * (t + 1.0))
                heapq.heappush(heap, (-delta, i))
        # Assign each extra student greedily to the class with current max delta
        for _ in range(extra_students):
            if not heap:
                break
            # Pop the class with highest current delta
            neg_delta, i = heapq.heappop(heap)
            # Assign student: increment pass and total
            classes[i][0] += 1
            classes[i][1] += 1
            # Recalculate delta with updated total (fail count remains constant)
            t = classes[i][1]
            delta = (t - classes[i][0]) / (t * (t + 1.0))
            # Push updated class back into heap
            heapq.heappush(heap, (-delta, i))
        # Compute sum of all class ratios
        total = 0.0
        for p, t in classes:
            total += p / t
        # Return average ratio
        return total / len(classes)

    maxAverageRatio = max_average_ratio
