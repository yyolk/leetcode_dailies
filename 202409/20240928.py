# https://leetcode.com/problems/design-circular-deque/


class MyCircularDeque:
    """859. Design Circular Deque

    Design your implementation of the circular double\\-ended queue (deque).

    Implement the `MyCircularDeque` class:

    * `MyCircularDeque(int k)` Initializes the deque with a maximum size of `k`.

    * `boolean insertFront()` Adds an item at the front of Deque. Returns `true` if the
    operation is successful, or `false` otherwise.

    * `boolean insertLast()` Adds an item at the rear of Deque. Returns `true` if the
    operation is successful, or `false` otherwise.

    * `boolean deleteFront()` Deletes an item from the front of Deque. Returns `true` if
    the operation is successful, or `false` otherwise.

    * `boolean deleteLast()` Deletes an item from the rear of Deque. Returns `true` if
    the operation is successful, or `false` otherwise.

    * `int getFront()` Returns the front item from the Deque. Returns `-1` if the deque
    is empty.

    * `int getRear()` Returns the last item from Deque. Returns `-1` if the deque is
    empty.

    * `boolean isEmpty()` Returns `true` if the deque is empty, or `false` otherwise.

    * `boolean isFull()` Returns `true` if the deque is full, or `false` otherwise.

    Your MyCircularDeque object will be instantiated and called as such:
        obj = MyCircularDeque(k)
        param_1 = obj.insertFront(value)
        param_2 = obj.insertLast(value)
        param_3 = obj.deleteFront()
        param_4 = obj.deleteLast()
        param_5 = obj.getFront()
        param_6 = obj.getRear()
        param_7 = obj.isEmpty()
        param_8 = obj.isFull()
    """
    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.size = 0
        self.capacity = k
        self.front = self.rear = 0
        self.data = [0] * k

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque. Returns -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self) -> int:
        """
        Get the last item from the deque. Returns -1 if the deque is empty.
        """
        if self.isEmpty():
            return -1
        # Since rear points to the next position where an element would be inserted,
        # we adjust it to point to the actual last element.
        return self.data[(self.rear - 1) % self.capacity]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.capacity