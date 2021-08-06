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