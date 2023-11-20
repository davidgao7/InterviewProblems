# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list. A node in a singly linked list should have two
# attributes: val and next. val is the value of the current node, and next is a pointer/
# reference to the next node. If you want to use the doubly linked list, you will
# need one more attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.
#
#  Implement the MyLinkedList class:
#
#
#  MyLinkedList() Initializes the MyLinkedList object.
#  int get(int index) Get the value of the indexᵗʰ node in the linked list. If
# the index is invalid, return -1.
#  void addAtHead(int val) Add a node of value val before the first element of
# the linked list. After the insertion, the new node will be the first node of the
# linked list.
#  void addAtTail(int val) Append a node of value val as the last element of
# the linked list.
#  void addAtIndex(int index, int val) Add a node of value val before the indexᵗ
# ʰ node in the linked list. If index equals the length of the linked list, the
# node will be appended to the end of the linked list. If index is greater than the
# length, the node will not be inserted.
#  void deleteAtIndex(int index) Delete the indexᵗʰ node in the linked list, if
# the index is valid.
#
#
#
#  Example 1:
#
#
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get",
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
#
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#
#
#
#  Constraints:
#
#
#  0 <= index, val <= 1000
#  Please do not use the built-in LinkedList library.
#  At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and
# deleteAtIndex.
#
#
#  Related Topics Linked List Design 👍 2474 👎 1550


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    def __init__(self):
        # create the dummy head, to represent the linked list from the start
        self.dummy_head = Node()
        # record the linked list size
        self.size = 0

    def get(self, index: int) -> int:
        #  int get(int index) Get the value of the indexᵗʰ node in the linked list. If
        # the index is invalid, return -1.
        if index < 0 or index >= self.size:
            return -1

        # get the index node value
        # update current ptr to the next of dummy
        current_ptr = self.dummy_head.next
        for i in range(index):  # 0..index-1, still index number of loops
            current_ptr = current_ptr.next

        return current_ptr.val  # return the loop till the index value

    def addAtHead(self, val: int) -> None:
        # no matter what youdo , not touch the first dummy head
        self.dummy_head.next = Node(
            val, self.dummy_head.next
        )  #  linked the node in front of first node, the order is correct since its not double direction linked list
        self.size += 1

    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        # out the loop, current will be the last element
        current.next = Node(
            val
        )  # will update the node in the linked list begin with dummy head
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # if the index is off the list len by 2 or more, is not possible to add at index
        if index < 0 or index > self.size:
            return

        current = self.dummy_head
        for i in range(index):
            current = current.next
        current.next = Node(val, current.next)  # current -> [new node] -> current.next
        # also update the size of the linked list
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # if the index is off the list len by 2 or more, is not possible to add at index
        if index < 0 or index >= self.size:  # remember that index range is [0, size-1]
            return

        current = self.dummy_head
        # loop till the one pervious of the node which need to be delete
        for i in range(index):
            current = current.next
        current.next = current.next.next  # delete the index node
        self.size-=1

    def return_result_linked_list_after_operation(self):
        return self.dummy_head



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    linklist = MyLinkedList()
    linklist.addAtTail(0)
    linklist.addAtTail(1)
    linklist.addAtTail(2)
    linklist.deleteAtIndex(1)
    pass