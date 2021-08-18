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
        # if only has one linked list
        if len(lists) == 1: return lists[0]
        # empty list case
        for list in lists:
            if not list:
                lists = lists[1:]
        if not lists:
            return

        # transform all linked list to list, sorting using merge sort / quick sort
        list_all = self.listsnode_to_list(lists)
        # only 1 elements in 2 lists
        if len(list_all) == 1 and list_all[0] is None: return None
        if len(list_all) == 1: return ListNode(lists[0].val)

        # quick sort
        low = 0
        high = len(list_all) - 1
        self.quick_sort(list_all, low, high)

        # transform list back to linked list
        result = self.list_to_node(list_all)
        return result

    def listsnode_to_list(self, lists: List[ListNode]):
        listall = []
        for node in lists:
            ref = node
            while ref:
                if ref.val != -1 or ref.val is not None:  # include 0
                    listall.append(ref.val)
                else:
                    pass
                ref = ref.next
        # for i in range(0, len(listall)):
        #     if i < len(listall) - 1 and listall[i] == 0:
        #         listall = listall[1:]
        return listall

    def list_to_node(self, list_sorted: List):
        result = ListNode(val=list_sorted[0])
        ref = result
        for i in range(1, len(list_sorted)):
            ref.next = ListNode(val=list_sorted[i])
            ref = ref.next
        return result

    def quick_sort(self, list, low, high):
        if high <= low:
            return list
        pivot = self.partition(list, low, high)
        self.quick_sort(list, low, pivot - 1)
        self.quick_sort(list, pivot + 1, high)

        # partition 大体和 mergesort 差不多，但不用 merge

        # take the last element as pivot, place at the correct position in arr

    def partition(self, list, low, high):  # e.g. [1,4,5,1,3,4,2,6], low:0 high:n-1
        pivot = high  # NOTE: always choose last one

        for i in range(low, high):
            if list[i] > list[pivot]:
                self.swap(list, i, pivot)

        return pivot

    def swap(self, list, idx, pivot):
        holder = list[idx]
        list[idx] = list[pivot]
        list[pivot] = holder


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
