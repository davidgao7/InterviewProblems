# Given a linked list, swap every two adjacent nodes and return its head. You
# must solve the problem without modifying the values in the list's nodes (i.e.,
# only nodes themselves may be changed.)
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#
#
#  Example 2:
#
#
# Input: head = []
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [1]
# Output: [1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 100].
#  0 <= Node.val <= 100
#
#
#  Related Topics Linked List Recursion 👍 11414 👎 417
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head  # finish looping or linked list is empty

        # define previous, current, next node, change point direction
        pre = head
        cur = head.next
        next = head.next.next

        # switch current and pre
        cur.next = pre
        # assign next as another group of 3 nodes start with pre for swap
        pre.next = self.swapPairs(next)  # Note: assign pre.next to the previous result

        return cur


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ex = ListNode(1,ListNode(2, ListNode(3, ListNode(4))))
    s = Solution()
    res = s.swapPairs(ex)
    pass