# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型二维数组
#
class PathSum:
    def path_sum(self, root, sum):
        # write code here
        temp, res = [], []

        def dfs(root, sum, cnt):
            if not root: return  # 如果节点为空结束当前递归
            temp.append(root.val)  # 将当前节点加入temp数组
            cnt += root.val  # 把当前节点加入到路径和中
            if root.left == None and root.right == None:  # 当递归到没有子树的时候就需要判断
                if cnt == sum: res.append(temp[:])  # 如果当前节点的路径和等于sum，那么就在res中插入tmp
            else:
                dfs(root.left, sum, cnt)  # 递归左子树
                dfs(root.right, sum, cnt)  # 递归右子树

            cnt -= temp[len(temp) - 1]
            temp.pop()

        dfs(root, sum, 0)
        return res
