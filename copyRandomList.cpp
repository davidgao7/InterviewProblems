//请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指
//向链表中的任意节点或者 null。
//
//
//
// 示例 1：
//
//
//
// 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
//输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
//
//
// 示例 2：
//
//
//
// 输入：head = [[1,1],[2,1]]
//输出：[[1,1],[2,1]]
//
//
// 示例 3：
//
//
//
// 输入：head = [[3,null],[3,0],[3,null]]
//输出：[[3,null],[3,0],[3,null]]
//
//
// 示例 4：
//
// 输入：head = []
//输出：[]
//解释：给定的链表为空（空指针），因此返回 null。
//
//
//
//
// 提示：
//
//
// -10000 <= Node.val <= 10000
// Node.random 为空（null）或指向链表中的节点。
// 节点数目不超过 1000 。
//
//
//
//
// 注意：本题与主站 138 题相同：https://leetcode-cn.com/problems/copy-list-with-random-
//pointer/
//
//
// Related Topics 哈希表 链表 👍 305 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
#include "iostream"

// Definition for a Node.
class Node {
public:
    int val;
    Node *next;
    Node *random;

    Node(int _val) {
        val = _val;
        next = nullptr;
        random = nullptr;
    }
};

class Solution {
private:
    int listLength(Node* node){
        int len = 0;
        Node* ref = node;
        while(ref){
            len++;
            ref = ref->next;
        }
        return len;
    }
public:
    void printNode(Node* node){
        int listLen = listLength(node);
        printf("node length is %d\n", listLen);
    }
    Node *copyRandomList(Node *head) {
        printf("working\n");
        return nullptr;
    }
};
//leetcode submit region end(Prohibit modification and deletion)

int main() {
    Solution *s = new Solution();
    // 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]: [value, loc index point to]
    //输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
    Node *head = new Node(7);
    Node *next1 = new Node(13);
    Node *next2 = new Node(11);
    Node *next3 = new Node(10);
    Node *next4 = new Node(1);

    // link linked list
    head->next = next1;
    next1->next = next2;
    next2->next = next3;
    next3->next = next4;
    next4->next = nullptr;

    head->random = nullptr;
    next1->random = head;
    next2->random = next4;
    next3->random = next2;
    next4->random = head;

//    s->printNode(head);
}

