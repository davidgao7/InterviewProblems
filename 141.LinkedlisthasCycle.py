class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param head ListNode类
# @return bool布尔型
#
class Solution:
    def hasCycle(self, head):  # TODO: not working
        # write code here
        if not head:
            return False
        st = {head.val}
        has_cycle = False
        while head.next:
            if not st.__contains__(head.next.val):
                st.add(head.next.val)
                head = head.next
            else:
                has_cycle = True
                break
        return has_cycle

    def hasCycle2(self, head):
        # use slow fast pointer
        if not head:
            return False
        # slow jump 1, fast jump 2
        slow, fast = head, head
        # the slow and fast will eventually meet if in cycle(if there's a cycle in linked list)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # slow, fast meet, cycle
            if slow == fast:
                return True

        return False


node1 = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None
s = Solution()
print(s.hasCycle(node1))
