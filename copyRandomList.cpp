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
#include <vector>
#include "unordered_map"

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
    int listLength(Node *node) {
        int len = 0;
        Node *ref = node;
        while (ref) {
            len++;
            ref = ref->next;
        }
        return len;
    }


public:
//    Node *copyRandomList(Node *head) {
//        if (head == nullptr) { return nullptr; }
//        Node *copy = new Node(0);
//        Node *ptr = copy;
//        while (head) {
//            ptr->val = head->val;
//            ptr->next = head->next;
//            ptr->random = head->random;
//            head = head->next;
//            ptr = ptr->next;
//        }
//        return copy;
//    }

/* NOTE:
 * If you are going to build large table once and do lots of queries, use std::unordered_map.
 * If you are going to build small table (may be under 100 elements) and do lots of queries,
 * use std::map .
 *
 * This is because reads on it are O(log n) .
 * If you are going to change table a lot then may be std::map is good option.
 * */
    Node *copyRandomList(Node *head) {
        if (head == nullptr) return nullptr;
        Node *cur = head;
        std::unordered_map<Node *, Node *> map;
        // large table-> std::unordered_map, small table(under 100 elements)->std::map because it reads in O(log n)
        // if going to change table a lot -> std::map
        // 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        while (cur != nullptr) {
            map[cur] = new Node(cur->val); // broke the node connection, store into map
            cur = cur->next;
        }
        cur = head;
        // 4. 构建新链表的 next 和 random 指向
        while (cur != nullptr) {
            map[cur]->next = map[cur->next]; //map[cur] is a node, cur is a node, reconstruct current->next node connection
            map[cur]->random = map[cur->random];
            cur = cur->next;
        }
        // 5. 返回新链表的头节点
        return map[head];
    }

    void printNode(Node *node) {
        printf("node value:\n");
        Node *ref = node;
        printf("[");
        while (ref) {
            if (ref->next == nullptr) {
                printf("%d", ref->val);
            } else {
                printf("%d->", ref->val);
            }
            ref = ref->next;
        }
        printf("]\n");

        printf("node random value\n");
        ref = node;
        printf("[");
        while (ref) {
            if (ref->random == nullptr) {
                printf("null, ");
            } else {
                printf("%d, ", ref->random->val);
            }
            ref = ref->next;
        }
        printf("]\n");
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

    printf("head node:\n");
    s->printNode(head);

    Node *result = s->copyRandomList(head);
    printf("result Node:\n");
    s->printNode(result);

}

