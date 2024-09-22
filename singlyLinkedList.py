"""
Design Singly Linked List

Design a Singly Linked List class.

Your LinkedList class should support the following operations:

    LinkedList() will initialize an empty linked list.
    int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    void insertHead(int val) will insert a node with val at the head of the list.
    void insertTail(int val) will insert a node with val at the tail of the list.
    bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

Example 1:

Input:
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]

Output:
[null, null, null, true, [0, 2]]

Example 2:

Input:
["insertHead", 1, "insertHead", 2, "get", 5]

Output:
[null, null, -1]

Note:

    The index int i provided to get(int i) and remove(int i) is guranteed to be greater than or equal to 0.
"""

from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1)  # dummy node

    def get(self, index: int) -> int:
        ptr = self.head.next  # skip dummy node

        i = 0
        while ptr:
            if i == index:
                # find the node at index, linked list do have this long
                # won't happend index > len(linkedlist)
                return ptr.val
            i += 1
            ptr = ptr.next
        return -1  # index out of bounds

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)  # our new head

        new_node.next = self.head.next  # since our head is a dummy node

        self.head.next = new_node
