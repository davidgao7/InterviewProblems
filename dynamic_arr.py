"""
Design Dynamic Array (Resizable Array)

Design a Dynamic Array (aka a resizable array) class, such as an ArrayList in Java or a vector in C++.

Your DynamicArray class should support the following operations:

    DynamicArray(int capacity) will initialize an empty array with a capacity of capacity, where capacity > 0.
    int get(int i) will return the element at index i. Assume that index i is valid.
    void set(int i, int n) will set the element at index i to n. Assume that index i is valid.
    void pushback(int n) will push the element n to the end of the array.
    int popback() will pop and return the element at the end of the array. Assume that the array is non-empty.
    void resize() will double the capacity of the array.
    int getSize() will return the number of elements in the array.
    int getCapacity() will return the capacity of the array.

If we call void pushback(int n) but the array is full, we should resize the array first.

Example 1:

Input:
["Array", 1, "getSize", "getCapacity"]

Output:
[null, 0, 1]

Example 2:

Input:
["Array", 1, "pushback", 1, "getCapacity", "pushback", 2, "getCapacity"]

Output:
[null, null, 1, null, 2]

Example 3:

Input:
["Array", 1, "getSize", "getCapacity", "pushback", 1, "getSize", "getCapacity", "pushback", 2, "getSize", "getCapacity", "get", 1, "set", 1, 3, "get", 1, "popback", "getSize", "getCapacity"]

Output:
[null, 0, 1, null, 1, 1, null, 2, 2, 2, null, 3, 3, 1, 2]

Note:

    The index i provided to get(int i) and set(int i) is guranteed to be greater than or equal to 0 and less than the number of elements in the array.
"""


class DynamicArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0

    def get(self, i: int) -> int:
        """
        will return the element at index i. Assume that index i is valid.
        """
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        """
        will set the element at index i to n. Assume that index i is valid.
        """
        if self.arr[i] is None:
            self.size += 1
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        """
        will push the element n to the end of the array.
        """
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        """
        will pop and return the element at the end of the array. Assume that the array is non-empty.
        """
        self.size -= 1
        # print(self.arr)
        return self.arr[self.size]

    def resize(self) -> None:
        """
        will double the capacity of the array.
        """
        # NOTE: array extend is not correct, use this silly way to copy and expand the array
        new_arr = [None] * self.capacity * 2
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity *= 2

    def getSize(self) -> int:
        """will return the number of elements in the array."""
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


if __name__ == "__main__":
    array = DynamicArray(4)

    array.pushback(1)
    array.set(0, 0)
    array.pushback(2)
    print(array.get(0))  # 0
    print(array.get(1))  # 2
    print(array.getCapacity())  # 4
    print(array.popback())  # 2
