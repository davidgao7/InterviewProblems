# Given the head of a singly linked list, reverse the list, and return the reversed list.
# Example 1:
#
#
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Example 2:
#
#
# Input: head = [1,2]
# Output: [2,1]
# Example 3:
#
# Input: head = []
# Output: []


# Definition for singly-linked list
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # NOTE: You should memorize this solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # set prev to None

        while head:
            temp = head.next  # set temp to head.next
            # reverse the rest of the list
            head.next = prev
            # set prev to head, loop rest of the list
            prev = head
            head = temp
        return prev

    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=" -> ")
            head = head.next
        # print("None")


if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(Solution().printList(Solution().reverseList(head)))  # 5 -> 4 -> 3 -> 2 -> 1
    head = ListNode(1, ListNode(2))
    print(Solution().printList(Solution().reverseList(head)))  # 2 -> 1
    head = ListNode()
    print(Solution().printList(Solution().reverseList(head)))  # None
