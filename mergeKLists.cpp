//
// Created by Tengjun Gao on 8/19/21.
//

#include "mergeKLists.h"
#include <vector>
#include <clocale>

//* Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    explicit ListNode(int x) : val(x), next(nullptr) {}
};

// 这个时候有 pointer和库的cpp应该比较好解决linked list

class mergeKLists {}; // 不用管

class Solution{
public:
    ListNode* mergeKLists(std::vector<ListNode*>& lists){
        return merge(lists, 0, lists.size() - 1);
    }

private:
    ListNode* merge(std::vector<ListNode*>& lists, int l, int r){
        
    }

    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2){}

};