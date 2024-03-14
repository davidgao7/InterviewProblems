# You are given the head of a singly linked-list. The list can be represented as:
#
# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:
#
# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [1,4,2,3]
# Example 2:
#
#
# Input: head = [1,2,3,4,5]
# Output: [1,5,2,4,3]
#
#
# Constraints:
#
# The number of nodes in the list is in the range [1, 5 * 104].
# 1 <= Node.val <= 1000
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    idea:
    1.break the linked list into two halfs using fast|slow pointers
    2.reverse the second half
    3.merge the two halfs

    12345 -> 123+45
    45 -> 54
    123, 54
      s   f

    1->5, 2->4, 3
    1->5->2->4->3
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        self.reverse(head)

    def reverse(self, head):
        dummy = ListNode(0, head)
        # initialize the fast and slow pointers
        fast, slow = dummy, head

        # find the pivot(slow)
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        # slow point to the 3 (pivot)
        print("slow: ", slow.val)
        print("fast: ", fast.val)

        print("====reversethe second half====")
        # reverse the second half
        #        4 -> 5 -> None   [slow]
        #  0 -> 4 -> 5 -> None   [slow]
        # prev cur
        #
        #  0 <- 4 <- 5 <- None
        # 5 -> 4 -> None
        # reverse the linked list (slow)
        prev, cur = None, slow.next
        while cur:
            # 1. save the next node
            next = cur.next
            # 2. reverse the pointer
            cur.next = prev
            # 3. move the pointers
            prev = cur
            cur = next

        print("==slow==")
        self.printList(slow)
        # merge the two halfs, and pivoit if the length is odd

    def printList(self, head):
        """
        print the linked list
        """
        while head:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    s.printList(head)
    s.reorderList(head)
    # Output: [1,4,2,3]
    # head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    # s.reorderList(head)
    # s.printList(head)
    # Output: [1,5,2,4,3]
