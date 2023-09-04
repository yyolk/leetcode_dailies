# https://leetcode.com/problems/implement-stack-using-queues/
"""225. Implement Stack using Queues

Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

Implement the `MyStack` class:
- `void push(int x)` Pushes element x to the top of the stack.
- `int pop()` Removes the element on the top of the stack and returns it.
- `int top()` Returns the element on the top of the stack.
- `boolean empty()` Returns true if the stack is empty, false otherwise.

Notes:
    You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""

# from collections import deque


# 33ms,30ms,37ms
class MyStack:
    def __init__(self):
        self._stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)

    def pop(self) -> int:
        return self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def empty(self) -> bool:
        return not self._stack


# 44ms, 45ms
# class MyStack:
#     def __init__(self):
#         self.queue1 = deque()  # Main storage queue
#         self.queue2 = deque()  # Temp queue for push

#     def push(self, x: int) -> None:
#         # Move all elements from queue1 to queue2
#         while self.queue1:
#             self.queue2.append(self.queue1.popleft())

#         # Add the new element to the front of the queue1
#         self.queue1.append(x)

#         # Move elements back from queue2 to queue1
#         while self.queue2:
#             self.queue1.append(self.queue2.popleft())

#     def pop(self) -> int:
#         # if self.queue1:
#         return self.queue1.popleft()
#         # return None

#     def top(self) -> int:
#         return self.queue1[0]

#     def empty(self) -> bool:
#         return not self.queue1


# 40ms
# Using one queue
# class MyStack:
#     def __init__(self):
#         self.queue = deque()

#     def push(self, x: int) -> None:
#         self.queue.append(x)
#         # Reverse the order of elements in the queue
#         for _ in range(len(self.queue) - 1):
#             self.queue.append(self.queue.popleft())

#     def pop(self) -> int:
#         if self.queue:
#             return self.queue.popleft()
#         return None

#     def top(self) -> int:
#         if self.queue:
#             return self.queue[0]
#         return None

#     def empty(self) -> bool:
#         return not self.queue


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
