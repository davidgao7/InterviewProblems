# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead:
            return pHead
        reverse = []
        while pHead:
            reverse.append(pHead.val)
            pHead = pHead.next

        reverse.reverse()
        reverseNode = ListNode(reverse[0])
        intermedeateNode = reverseNode

        for i in range(1, len(reverse)):
            node = ListNode(reverse[i])
            intermedeateNode.next = node
            intermedeateNode = intermedeateNode.next

        intermedeateNode.next = None
        return reverseNode

    def reverse_link_list_regular(self, head):
        # 1. decleare a pre node to help curr node reverse point
        cur=head
        pre = None
        # 2. loop through the linked list, reverse the list one by one
        while cur:
            # 2.1 flip the cur
            temp = cur.next
            cur.next = pre
            # 2.2 updatethe pre and cur
            pre = cur
            cur = temp

        return pre