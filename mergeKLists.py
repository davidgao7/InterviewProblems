# 给你一个链表数组，每个链表都已经按升序排列。
#
#  请你将所有链表合并到一个升序链表中，返回合并后的链表。
#
#
#
#  示例 1：
#
#  输入：lists = [[1,4,5],[1,3,4],[2,6]]
# 输出：[1,1,2,3,4,4,5,6]
# 解释：链表数组如下：
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 将它们合并到一个有序链表中得到。
# 1->1->2->3->4->4->5->6
#
#
#  示例 2：
#
#  输入：lists = []
# 输出：[]
#
#
#  示例 3：
#
#  输入：lists = [[]]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  k == lists.length
#  0 <= k <= 10^4
#  0 <= lists[i].length <= 500
#  -10^4 <= lists[i][j] <= 10^4
#  lists[i] 按 升序 排列
#  lists[i].length 的总和不超过 10^4
#
#  Related Topics 链表 分治 堆（优先队列） 归并排序
#  👍 1454 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        x = None  # 相当于nullptr, 从什么都没有开始合并
        for y in lists:
            x = self.merge(x, y)  # [ListNode1, ListNode2...], 从左到右两个两个合并
        return x  # 每次合并用mergesort

    def merge(self, a: ListNode, b: ListNode) -> ListNode:
        dummy = ListNode(-1)
        x = dummy  # x 是 dummy 的 ptr， 更新它会使得dummy一块更新，但是dummy一直指向第一个元素所以不会最后return空元素list！！
        while a and b: #每次比较都把小的放进去
            ############################################## determine next val in result,
            if a.val < b.val:                           ## continuing update ptr x to
                x.next = a                              ## append next node in
                a = a.next                              ##
            else:                                       ##
                x.next = b  # x 是dummy的ptr             ##
                b = b.next                              ##
            x = x.next                                  ## 把dummy开头的 -1 拿掉了，并且更新dummy，把之前的都去掉只给dummy要的
            ##############################################
        if a: ############################################ 处理｜a-b｜多的
            x.next = a                                   #
        if b:                                            #
            x.next = b                                   #
            ##############################################
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
# lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# linkedlist_1 = ListNode(
#     1, ListNode(
#         4,
#         ListNode(
#             5
#         )
#     )
# )
# linkedlist_2 = ListNode(1,
#                         ListNode(
#                             3, ListNode(4)
#                         ))
# linkedlist_3 = ListNode(2, ListNode(6))
s = Solution()


# lists = [linkedlist_1, linkedlist_2, linkedlist_3]
def print_linked_lists(lists):
    i = 0
    for node in lists:
        print("linked list %d" % i)
        list = []
        while node:
            list.append(node.val)
            node = node.next
        print(list)
        i += 1


def print_linked_list(node):
    list = []
    while node:
        list.append(node.val)
        node = node.next
    print(list)


node1 = ListNode(1,
                 ListNode(4,
                          ListNode(5))
                 )
node2 = ListNode(1,
                 ListNode(3,
                          ListNode(4))
                 )
node3 = ListNode(2,
                 ListNode(6)
                 )

lists = [node1, node2, node3]

print_linked_lists(lists)
result = s.mergeKLists(lists)
print("after merge:")
print_linked_list(result)
# 时间复杂度，空间复杂度
