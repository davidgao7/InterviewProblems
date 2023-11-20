# Given the head of a linked list and an integer val, remove all the nodes of
# the linked list that has Node.val == val, and return the new head.
#
#
#  Example 1:
#
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
#
#  Example 2:
#
#
# Input: head = [], val = 1
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [7,7,7,7], val = 7
# Output: []
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is in the range [0, 10⁴].
#  1 <= Node.val <= 50
#  0 <= val <= 50
#
#
#  Related Topics Linked List Recursion 👍 7925 👎 221
import copy
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy_head = ListNode(next=head)

        current = dummy_head  # physical address is the same
        while current.next:
            if current.next.val == val:
                # deletion
                current.next = current.next.next
            else:
                current = current.next  # current change but dummy_head not change. the physical address start to differ

        return dummy_head.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
    result = s.removeElements(head, 5)
    pass
