//
// Created by Tengjun Gao on 10/2/21.
//
/*
 * binary tree inorder, preorder and post order traversal
 * inorder: N L R
 * preorder: L N R
 * postorder: L R N*/
#include <stdio.h>
#include <vector>
#include <iostream>
#include <stack>

class TreeNode {
public:
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}

    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    std::vector<int> preorder(TreeNode* root) { //pass
        std::stack<TreeNode*> st;
        std::vector<int> result;
        if (root == nullptr) return result;
        st.push(root);
        while (!st.empty()) {
            TreeNode* node = st.top();                       // 中
            st.pop();
            result.push_back(node->val);
            if (node->right) st.push(node->right);           // 右（空节点不入栈）
            if (node->left) st.push(node->left);             // 左（空节点不入栈）
        }
        return result;
    }

    std::vector<int> inorder(TreeNode *root) {
        std::stack<TreeNode*> stack;
        std::vector<int> result;
        TreeNode* current = root;

        while(current != nullptr || !stack.empty()){
            if (current != nullptr){
                stack.push(current); // add e at the Top of the stack O(1)
                current = current->left;
            }else{
                current = stack.top(); // return a reference to the top most e of stack O(1)
                stack.pop(); // deletes the top most e of stack O(1)
                result.push_back(current->val);
                current = current->right;
            }
        }
        return result;
    }

    std::vector<int> postorder(TreeNode *root) {
        // 改preorder
        std::stack<TreeNode*> stack;
        std::vector<int> result;
        if (root == nullptr) return result;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            result.push_back(node->val);
            if (node->left) stack.push(node->left);
            if (node->right) stack.push(node->right);
        }
        reverse(result.begin(), result.end());
        return result;
    }

    void printVecotr(std::vector<int> arr) {
        std::cout << '[';
        for (int i = 0; i < arr.size(); i++) {
            std::cout << arr[i] << ',' << ' ';
        }
        std::cout << ']';
    }

};

int main() {
    Solution *solution = new Solution();
    int Tree_arr[5] = {1, -1, 0, 0, 1}; // fix sized arr
    TreeNode *input = new TreeNode(Tree_arr[0]);
    input->left = new TreeNode(Tree_arr[1]);
    input->right = new TreeNode(Tree_arr[2]);
    input->left->left = new TreeNode(Tree_arr[3]);
    input->right->left = new TreeNode(Tree_arr[4]);

    printf("preorder of the tree[L N R]:\n");
    std::vector<int> preorder = {};
    preorder = solution->preorder(input);
    solution->printVecotr(preorder);

    printf("\ninorder of the tree[N L R]:\n");
    std::vector<int> inorder = {};
    inorder = solution->inorder(input);
    solution->printVecotr(inorder);

    printf("\npostorder of the tree[L R N]:\n");
    std::vector<int> postorder = {};
    postorder = solution->postorder(input);
    solution->printVecotr(postorder);
}
