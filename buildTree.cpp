//输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
//
// 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
//
//
//
// 示例 1:
//
//
//Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
//Output: [3,9,20,null,null,15,7]
//
//
// 示例 2:
//
//
//Input: preorder = [-1], inorder = [-1]
//Output: [-1]
//
//
//
//
// 限制：
//
// 0 <= 节点个数 <= 5000
//
//
//
// 注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
//preorder-and-inorder-traversal/
// Related Topics 树 数组 哈希表 分治 二叉树 👍 585 👎 0


//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
using namespace std;

#include <iostream>
#include "vector"
#include <stack>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
public:
    TreeNode* buildTree(vector<int> &preorder, vector<int> &inorder) {
        // preorder: N L R [中 左 右]
        // inorder: L N R [左 中 右]
        // postorder: L R N [左 右 中]

        // 1. get the root node from preorder(中 左 右)
        TreeNode *root = new TreeNode(preorder[0]);
        // 2. split node into [left root right] parts (inorder)
        vector<int> left, right;
        bool flag = true;
        for (int i = 0; i < inorder.size(); i++) {
            if (inorder[i] != preorder[0] && flag) { // left
                left.push_back(inorder[i]);
            }
            if (inorder[i] == preorder[0]) {
                flag = false;
            }
            if (inorder[i] != preorder[0] && !flag) { // right
                right.push_back(inorder[i]);
            }
        }

        return root;
    }

    void postOrderPrintTree(TreeNode* root){
        std::stack<TreeNode*> stack;
        std::vector<int> result;
        if (root == nullptr) return;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode* node = stack.top();
            stack.pop();
            result.push_back(node->val);
            if (node->left) stack.push(node->left);
            if (node->right) stack.push(node->right);
        }
        reverse(result.begin(), result.end());
        printVecotr(result);
    }

    void printVecotr(std::vector<int> arr) {
        std::cout << '[';
        for (int i = 0; i < arr.size(); i++) {
            std::cout << arr[i] << ',' << ' ';
        }
        std::cout << ']';
    }
};
//leetcode submit region end(Prohibit modification and deletion)
int main() {
    vector<int>preorder = {3,9,20,15,7};
    vector<int>inorder = {9,3,15,20,7};
    Solution* solurtion = new Solution();
    TreeNode* answer = solurtion->buildTree(preorder, inorder);
    solurtion->postOrderPrintTree(answer);
};