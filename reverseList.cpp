//
// Created by Tengjun Gao on 11/28/21.
//

//给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
//
//
//
//
// 示例 1：
//
//
//输入：head = [1,2,3,4,5]
//输出：[5,4,3,2,1]
//
//
// 示例 2：
//
//
//输入：head = [1,2]
//输出：[2,1]
//
//
// 示例 3：
//
//
//输入：head = []
//输出：[]
//
//
//
//
// 提示：
//
//
// 链表中节点的数目范围是 [0, 5000]
// -5000 <= Node.val <= 5000
//
//
//
//
// 进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
//
//
// Related Topics 递归 链表 👍 2118 👎 0
#include <stdio.h>
#include <stack>

using namespace std;

//leetcode submit region begin(Prohibit modification and deletion)

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *reverseList(ListNode *head) {
        // cur, pre 两个 两个反转
        // 先开始， pre=nullptr, cur=first node,向右移动cur，再向右移动pre，将cur指向pre完成反转，最后 pre=last node, cur=nullptr表明已经遍历所有node，整个链表已经完成反转
        if (!head) return nullptr;

        ListNode *temp; // point to next
        ListNode *cur = head; // current ptr
        ListNode *pre = nullptr; // previous e ptr

        while (cur) {
            temp = cur->next; // store next state
            cur->next = pre; // reverse point direction

            pre = cur; // move pre to the right (origin link list direction)
            cur = temp; // move current to the right (next element)
        }

        // when cur = nullptr, out while loop, pre point to one behind cur,which is the head of the reversed list
        return pre;
    }

    void printList(ListNode *head) {
        while (head != nullptr) {
            printf("%d->", head->val);
            head = head->next;
        }
        printf("\n");
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    ListNode *head = new ListNode(1, new ListNode(2,
                                                  new ListNode(3,
                                                               new ListNode(4,
                                                                            nullptr))));
    Solution *s = new Solution();
    s->printList(head);
    ListNode *result = s->reverseList(head);
    s->printList(result);
}