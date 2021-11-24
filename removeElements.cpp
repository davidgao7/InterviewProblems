//
// Created by Tengjun Gao on 11/24/21.
//

//给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
//
//
// 示例 1：
//
//
//输入：head = [1,2,6,3,4,5,6], val = 6
//输出：[1,2,3,4,5]
//
//
// 示例 2：
//
//
//输入：head = [], val = 1
//输出：[]
//
//
// 示例 3：
//
//
//输入：head = [7,7,7,7], val = 7
//输出：[]
//
//
//
//
// 提示：
//
//
// 列表中的节点数目在范围 [0, 10⁴] 内
// 1 <= Node.val <= 50
// 0 <= val <= 50
//
// Related Topics 递归 链表 👍 740 👎 0
#include <iostream>

//leetcode submit region begin(Prohibit modification and deletion)

// * Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}

    ListNode(int x) : val(x), next(nullptr) {}

    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode *removeElements(ListNode *head, int val) {

        ListNode* dummy = new ListNode(0);
        dummy->next = head; // 防止while少算一个
        ListNode *cur = dummy; // ptr for looping

        while(cur->next != nullptr){
            if (cur->next->val == val){
                // delete one node including its memory
                ListNode* tmp = cur->next;
                cur->next = cur->next->next; // delete the head
                delete tmp;
            }else{
                cur = cur->next;
            }
        }

        head = dummy->next; // delete the initial 0 at the beginning of dummy
        delete dummy;
        return head;
    }

    void printElement(ListNode *node){
        ListNode *ref = node;
        printf("[");
        while(ref->next != nullptr){
            printf("%d->", ref->val);
            ref = ref->next;
        }
        printf("%d]\n", ref->val);
    }
};

//leetcode submit region end(Prohibit modification and deletion)
int main() {
    Solution *s = new Solution();
    ListNode *input = new ListNode(7,
                                   new ListNode(7,
                                                new ListNode(8)));
    s->printElement(input);
    ListNode *answer =  s->removeElements(input, 7);
    s->printElement(answer);
}