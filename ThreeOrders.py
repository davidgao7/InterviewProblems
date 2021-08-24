class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#
#
# @param root TreeNode类 the root of binary tree
# @return int整型二维数组
#
class Solution:
    def __init__(self):
        self.inorder = []
        self.postorder = []
        self.preorder = []

    def threeOrders(self, root):
        # write code here
        self.pre_order(root)
        self.in_order(root)
        self.post_order(root)

        return [self.preorder, self.inorder, self.postorder]

    def pre_order(self, root):
        # L N R
        if root.left is not None:
            self.pre_order(root.left)
        if root is not None:
            self.preorder.append(root.val)
        if root.right is not None:
            self.pre_order(root.right)


    def in_order(self, root):
        # N L R
        if root is not None:
            self.inorder.append(root.val)
        if root.left is not None:
            self.in_order(root.left)
        if root.right is not None:
            self.in_order(root.right)

    def post_order(self, root):
        # L R N
        if root.left is not None:
            self.post_order(root.left)
        if root.right is not None:
            self.post_order(root.right)
        if root is not None:
            self.postorder.append(root.val)

root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right
solution = Solution()
solution.pre_order(root)
solution.in_order(root)
solution.post_order(root)
print(solution.inorder)
print(solution.preorder)
print(solution.postorder)