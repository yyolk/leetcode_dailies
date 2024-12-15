# https://leetcode.com/problems/maximum-average-pass-ratio/


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
    ) -> float: ...

    maxAverageRatio = max_average_ratio
