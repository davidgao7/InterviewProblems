//
// Created by Tengjun Gao on 8/19/21.
//

#include <vector>
#include <clocale>

//* Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;

    explicit ListNode(int x) : val(x), next(nullptr) {}
};

// 这个时候有 pointer和库的cpp应该比较好解决linked list

class mergeKLists {
}; // 不用管

class Solution {
public:
    ListNode *mergeKLists(std::vector<ListNode *> &lists) {
        return merge(lists, 0, lists.size() - 1);
    }

    static void printNodeval(ListNode *node) {
        // & ref, * pointer

        ListNode *refnode = node;
        printf("[");
        while (refnode->next != nullptr) {
            printf("%d,", refnode->val);
            refnode = refnode->next;
        }
        printf("%d", refnode->val); // print last val
        printf("]\n");
    }

    static void printListNodes(std::vector<ListNode *> &lists) {
        for (int i = 0; i < lists.size(); i++) {
            printf("list %d:\n", i);
            printNodeval(lists[i]);
        }
    }

private:


    ListNode *merge(std::vector<ListNode *> &lists, int left, int right) {

        // base case
        if (left > right) return nullptr;
        if (left == right) return lists[left];
        if (left + 1 == right) return mergeTwoLists(lists[left], lists[right]);

        // divide & conquer
        int mid = int(left + (right - left) / 2);
        ListNode *r1 = merge(lists, left, mid);
        ListNode *r2 = merge(lists, mid + 1, right);

        ListNode *result = mergeTwoLists(r1, r2);
        return result;
    }

    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {

        // loop and compare , merge to one list
        ListNode result(0); // new object in memory
        ListNode *ptr = &result; // ptr to result memory location

        // if compare index by index, I think we won't know the real smaller one
        /*eg
         * [1,2,3,4,5]
         * [3,7]
         *
         * In this case, if we did "indexly", will be
         * [1,3,2,7,3,4,5],
         * 1. 1 compares with 3: [1,3]
         * 2. 2 compares with 7: [2,7], then combine tail with step 1: [1,3,2,7]
         * 3. and so on
         * */
        // therefore, we need to compare one node with every (half) node in the other list
         while (l1 && l2) {
           if (l1->val < l2->val) {
              ptr->next = l1;
              l1 = l1->next;
           }
           else{
             ptr->next = l2;
             l2 = l2->next;
           }
           ptr->next = l1;
           l1 = l1->next;
           ptr = ptr->next;
         }
         if (l1) ptr->next = l1;
         if (l2) ptr->next = l2;
         return result.next;
    }


};

int main() {
    Solution *solution = new Solution();

    // 1 -> 4 -> 5
    ListNode *l1 = new ListNode(1);
    ListNode *n2 = new ListNode(4);
    ListNode *n3 = new ListNode(5);
    l1->next = n2;
    n2->next = n3;

    // 1 -> 3 -> 4
    ListNode *l2 = new ListNode(1);
    ListNode *n4 = new ListNode(3);
    ListNode *n5 = new ListNode(4);
    l2->next = n4;
    n4->next = n5;

    // 2 -> 6
    ListNode *l3 = new ListNode(2);
    ListNode *n6 = new ListNode(6);
    l3->next = n6;

    // result
    std::vector<ListNode *> listsOfLinkedList;
    listsOfLinkedList.push_back(l1);
    listsOfLinkedList.push_back(l2);
    listsOfLinkedList.push_back(l3);

    solution->printListNodes(listsOfLinkedList);
    ListNode *reuslt = solution->mergeKLists(listsOfLinkedList); // pointer

    printf("\nmerge K lists:\n");
    Solution::printNodeval(reuslt);

}
