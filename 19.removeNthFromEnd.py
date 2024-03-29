# Given the head of a linked list, remove the nᵗʰ node from the end of the list
# and return its head.
#
#
#  Example 1:
#
#
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#
#
#  Example 2:
#
#
# Input: head = [1], n = 1
# Output: []
#
#
#  Example 3:
#
#
# Input: head = [1,2], n = 1
# Output: [1]
#
#
#
#  Constraints:
#
#
#  The number of nodes in the list is sz.
#  1 <= sz <= 30
#  0 <= Node.val <= 100
#  1 <= n <= sz
#
#
#
#  Follow up: Could you do this in one pass?
#
#  Related Topics Linked List Two Pointers 👍 17530 👎 729
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use fast and slow pointer, start from dummy
        # make a dummyhead at the front
        dummy = ListNode(next=head)
        fast, slow = dummy, dummy  # both fast and slow start with dummy

        # let fast go through n+1 nodes since we add a dummy node
        while n+1 > 0:
            fast = fast.next
            n -= 1

        # fast is pointing to the target node pervious one right now,
        # move both slow and fast node until fast finish the list
        while fast:
            slow = slow.next
            fast = fast.next

        # right now, the fast point to null, slow point to the one before the target node!
        # delete the node
        slow.next = slow.next.next
        return dummy.next

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    head = ListNode(1,
                    ListNode(2,
                             ListNode(3,
                                      ListNode(4,
                                               ListNode(5)))))
    result = s.removeNthFromEnd(head, 2)
    print(result)
