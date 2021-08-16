# 描述
# 给定一个二叉树，返回该二叉树层序遍历的结果，（从左到右，一层一层地遍历）
# 例如：
# 给定的二叉树是{3,9,20,#,#,15,7},
#  3
# / \
# 9 20
#  / \
# 15  7
# 该二叉树层序遍历的结果是
# [
# [3],
# [9,20],
# [15,7]
# ]
# 示例1
# 输入：{1,2}
# 返回值：[[1],[2]]
# 示例2
# 输入：{1,2,3,4,#,#,5}
# 返回值：[[1],[2,3],[4,5]]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# @param root TreeNode类
# @return int整型二维数组
#
class Solution:
    def levelOrder(self, root):
        # write code here
        # N L R in order
        if not root:
            return []

        quene = [root]
        out_list = []

        while quene:
            length = len(quene)
            in_list = []
            for _ in range(length):
                curnode = quene.pop(0)  # （默认移除列表最后一个元素）这里需要移除队列最头上的那个
                in_list.append(curnode.val) # 1st get left val, then got right val: [level0:l, level1:l,r, level2:l,r...]
                if curnode.left: quene.append(curnode.left) # first store left then right, same with in order
                if curnode.right: quene.append(curnode.right)
            out_list.append(in_list)

        return out_list



T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
T.right.left = TreeNode(4)
T.right.right = TreeNode(5)
s = Solution()
arryy = s.levelOrder(T)
print(arryy)
