# https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/
from collections import deque


class Solution:
    """1700. Number of Students Unable to Eat Lunch

    The school cafeteria offers circular and square sandwiches at lunch break, referred
    to by numbers `0` and `1` respectively. All students stand in a queue. Each student
    either prefers square or circular sandwiches.

    The number of sandwiches in the cafeteria is equal to the number of students. The
    sandwiches are placed in a **stack**. At each step:

    * If the student at the front of the queue **prefers** the sandwich on the top of
    the stack, they will **take it** and leave the queue.

    * Otherwise, they will **leave it** and go to the queue's end.

    This continues until none of the queue students want to take the top sandwich and
    are thus unable to eat.

    You are given two integer arrays `students` and `sandwiches` where `sandwiches[i]`
    is the type of the `i`^th^ sandwich in the stack (`i = 0` is the top of the
    stack) and `students[j]` is the preference of the `j`^th^ student in the initial
    queue (`j = 0` is the front of the queue). Return *the number of students that are
    unable to eat.*

    """

    def count_students(self, students: list[int], sandwiches: list[int]) -> int:
        """Alternative solution."""
        students_deque = deque(students)
        sandwiches_deque = deque(sandwiches)
        count, limit = 0, len(students_deque)

        # Loop through students and sandwiches
        while students_deque:
            n = len(students_deque)

            # If the count reaches the initial length of the queue, there are no more
            # possible matches
            if count == n:
                break

            # Get the current student and sandwich
            current_student = students_deque.popleft()
            current_sandwich = sandwiches_deque[0]

            # If the current student prefers the current sandwich, remove the sandwich
            if current_student == current_sandwich:
                sandwiches_deque.popleft()
                count, limit = 0, n
            # If the student does not prefer the sandwich, move them to the end of the queue
            else:
                students_deque.append(current_student)
                count += 1

        # Return the number of students left in the queue (unable to eat)
        return len(students_deque)

    countStudents = count_students

    def count_students_no_deque(self, students: list[int], sandwiches: list[int]) -> int:
        """First solution."""
        count = 0
        # Loop through students and sandwiches
        while len(students) > count:
            # If the student at the front of the queue prefers the sandwich on the top of the stack, remove the sandwich
            if students[0] == sandwiches[0]:
                sandwiches.pop(0)
                count = 0
            # If the student does not prefer the sandwich, move them to the end of the queue
            else:
                students.append(students[0])
                count+=1
            # Remove the student from the front of the queue
            students.pop(0)
        # Return the number of students left in the queue
        return len(students)
