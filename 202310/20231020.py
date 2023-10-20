# https://leetcode.com/problems/flatten-nested-list-iterator/
"""341. Flatten Nested List Iterator

You are given a nested list of integers `nestedList`. Each element is either an integer
or a list whose elements may also be integers or other lists. Implement an iterator to
flatten it.

Implement the `NestedIterator` class:

* `NestedIterator(List<NestedInteger> nestedList)` Initializes the iterator with the
   nested list `nestedList`.
* `int next()` Returns the next integer in the nested list.
* `boolean hasNext()` Returns `true` if there are still some integers in the nested
  list and `false` otherwise.

Your code will be tested with the following pseudocode:

    initialize iterator with nestedList
    res = []
    while iterator.hasNext()
        append iterator.next() to the end of res
    return res

Your `NestedIterator` object will be instantiated and called as such:

    i, v = NestedIterator(nestedList), []
    while i.hasNext(): v.append(i.next())

If `res` matches the expected flattened list, then your code will be judged as correct.

This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation:

    class NestedInteger:
        def isInteger(self) -> bool:
            '''
            @return True if this NestedInteger holds a single integer, rather than a nested list.
            '''

        def getInteger(self) -> int:
            '''
            @return the single integer that this NestedInteger holds, if it holds a single integer
            Return None if this NestedInteger holds a nested list
            '''

        def getList(self) -> [NestedInteger]:
            '''
            @return the nested list that this NestedInteger holds, if it holds a nested list
            Return None if this NestedInteger holds a single integer
            '''

"""


# Reflecting methods on NestedInteger for snake_case maximalism.
NestedInteger.is_integer = NestedInteger.isInteger
NestedInteger.get_integer = NestedInteger.getInteger
NestedInteger.get_list = NestedInteger.getList


class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        def flatten(nested_integers):
            result = []
            for nested_integer in nested_integers:
                if nested_integer.is_integer():
                    # If the NestedInteger is an integer, add it to the result.
                    result.append(nested_integer.get_integer())
                else:
                    # If it's a list, recursively flatten it and extend the result.
                    result.extend(flatten(nested_integer.get_list()))
            return result

        # Flatten the input nested list when the iterator is initialized.
        self.flattened = flatten(nested_list)
        # Initialize a pointer to keep track of the current position in flattened list.
        self.pointer = 0

    def next(self) -> int:
        # Increment the pointer and return the current integer.
        self.pointer += 1
        return self.flattened[self.pointer - 1]

    def has_next(self) -> bool:
        # Check if there are more integers in the flattened list.
        return self.pointer < len(self.flattened)

    # Reflecting 'hasNext' method for snake_case maximalism.
    hasNext = has_next
