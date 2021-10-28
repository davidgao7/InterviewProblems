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
#include "unordered_map"

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
private:
    unordered_map<int, int> index; // 通过map快速定位根结点

public:
    TreeNode *
    myBuildTree(vector<int> &preorder, vector<int> &inorder, int preorderLeft, int preorderRight, int inorderLeft,
                int inorderRight) {

        if (preorderLeft > preorderRight) return nullptr;

        // preorder: N L R [中 左 右]
        // inorder: L N R [左 中 右]
        // postorder: L R N [左 右 中]

        // preorder: root, left, right, the 1st node will be the root node
        int preorderRoot = preorderLeft;

        // find the root node in inorder list
        int inorderRoot = index[preorder[preorderRoot]]; // inorderRoot 的左边都是left sub tree

        // create root
        TreeNode *root = new TreeNode(preorder[preorderRoot]);

        // get left subtree size
        int leftSubTreeSize = inorderRoot - inorderLeft;

        // recursively create leftSub, then connect to root
        root->left = myBuildTree(
                preorder,
                inorder,
                preorderLeft + 1,
                preorderLeft + leftSubTreeSize,
                inorderLeft,
                inorderRoot - 1
        );

        // recursively create rightSub, then connect to root
        root->right = myBuildTree(
                preorder,
                inorder,
                preorderLeft + leftSubTreeSize + 1,
                preorderRight,
                inorderRoot + 1,
                inorderRight
        );

        return root;
    }

    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        int preorderSize = preorder.size();

        // map the index of inorder to find root node easily
        for (int i = 0; i < preorderSize; i++) {
            index[inorder[i]] = i;
        }

        return myBuildTree(preorder, inorder, 0, preorderSize - 1, 0, preorderSize - 1);
    }

    void postOrderPrintTree(TreeNode *root) {
        std::stack<TreeNode *> stack;
        std::vector<int> result;
        if (root == nullptr) return;
        stack.push(root);
        while (!stack.empty()) {
            TreeNode *node = stack.top();
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
    vector<int> preorder = {3, 9, 20, 15, 7};
    vector<int> inorder = {9, 3, 15, 20, 7};
    Solution *solurtion = new Solution();
    TreeNode *answer = solurtion->buildTree(preorder, inorder);
    solurtion->postOrderPrintTree(answer);
};