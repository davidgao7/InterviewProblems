# Given the head of a linked list, return the node where the cycle begins. If
# there is no cycle, return null.
#
#  There is a cycle in a linked list if there is some node in the list that can
# be reached again by continuously following the next pointer. Internally, pos is
# used to denote the index of the node that tail's next pointer is connected to (0
# -indexed). It is -1 if there is no cycle. Note that pos is not passed as a
# parameter.
#
#  Do not modify the linked list.
#
#
#  Example 1:
#
#
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the
# second node.
#
#
#  Example 2:
#

# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the
# first node.
#
#
#  Example 3:
#
#
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#
#
#
#  Constraints:
#
#
#  The number of the nodes in the list is in the range [0, 10⁴].
#  -10⁵ <= Node.val <= 10⁵
#  pos is -1 or a valid index in the linked-list.
#
#
#
#  Follow up: Can you solve it using O(1) (i.e. constant) memory?
#
#  Related Topics 哈希表 链表 双指针 👍 2334 👎 0
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # solution: fast and slow pointer
        # we define a slow and a fast pointer, both start from the head
        # move fast and slow at the same time, for every two steps fast take, slow will move one step forward
        # the cycle will be detected if fast and slow potiner meets!
        # stop condition: 1. when fast and slow meet 2. fast will always move to the end first , if fast move to the end,
        # there is no cycle

        slow, fast = head, head

        # fast will always move to the end first
        while fast and fast.next:

            # moving fast and slow ptr
            slow = slow.next
            fast = fast.next.next

            # if fast and slow meets,
            if fast == slow:
                # then launch two new ptrs, one start from head, another from where fast and slow meets
                slow = head
                # move slow and index2, the point they meet will be the cycle start point
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                # return the cycle start point
                return slow

        # if there's no cycle
        return None

if __name__ == '__main__':
    ex = ListNode(1,
                  ListNode(2)
                  )


