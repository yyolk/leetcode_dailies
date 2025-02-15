# https://leetcode.com/problems/product-of-the-last-k-numbers/
"""1477. Product of the Last K Numbers

Design an algorithm that accepts a stream of integers and retrieves the product of
the last `k` integers of the stream.

Implement the `ProductOfNumbers` class:

* `ProductOfNumbers()` Initializes the object with an empty stream.

* `void add(int num)` Appends the integer `num` to the stream.

* `int getProduct(int k)` Returns the product of the last `k` numbers in the current
list. You can assume that always the current list has at least `k` numbers.

The test cases are generated so that, at any time, the product of any contiguous
sequence of numbers will fit into a single 32-bit integer without overflowing.


Your ProductOfNumbers object will be instantiated and called as such:
    obj = ProductOfNumbers()
    obj.add(num)
    param_2 = obj.getProduct(k)
"""


class ProductOfNumbers:

    def __init__(self):
        # Initialize with 1 to handle the first product calculation
        self.prefix_products = [1]

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix products if the number is zero
            self.prefix_products = [1]
        else:
            # Append the product of the last prefix product and the new number
            self.prefix_products.append(self.prefix_products[-1] * num)

    def get_product(self, k: int) -> int:
        if k >= len(self.prefix_products):
            # If k is greater than or equal to the length of prefix_products, it means there was a zero in the last k numbers
            return 0
        else:
            # The product of the last k numbers is the last prefix product divided by the prefix product at (len - k - 1)
            return self.prefix_products[-1] // self.prefix_products[-k - 1]

    getProduct = get_product
