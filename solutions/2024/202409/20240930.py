# https://leetcode.com/problems/design-a-stack-with-increment-operation/


class CustomStack:
    """1497. Design a Stack With Increment Operation

    Design a stack that supports increment operations on its elements.

    Implement the `CustomStack` class:

    * `CustomStack(int maxSize)` Initializes the object with `maxSize` which is the
    maximum number of elements in the stack.

    * `void push(int x)` Adds `x` to the top of the stack if the stack has not reached
    the `maxSize`.

    * `int pop()` Pops and returns the top of the stack or `-1` if the stack is empty.

    * `void inc(int k, int val)` Increments the bottom `k` elements of the stack by
    `val`. If there are less than `k` elements in the stack, increment all the elements
    in the stack.

    Your CustomStack object will be instantiated and called as such:
        obj = CustomStack(maxSize)
        obj.push(x)
        param_2 = obj.pop()
        obj.increment(k,val)

    """

    def __init__(self, maxSize: int):
        # Initialize the stack with a list and store the max size
        self.stack = []
        self.maxSize = maxSize
        # Use another list to keep track of increment values
        self.inc = []

    def push(self, x: int) -> None:
        # Add x to the stack if not at max capacity
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            # Also initialize an increment value for this new element
            self.inc.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1

        # Index of the top element
        i = len(self.stack) - 1
        if i > 0:
            # Pass the increment value to the next element if it's not the last one
            self.inc[i - 1] += self.inc[i]

        # Pop the element and add any carried increment
        value = self.stack.pop() + self.inc.pop()
        return value

    def increment(self, k: int, val: int) -> None:
        # If the stack is empty or k is more than stack size, increment all or up to k
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val
