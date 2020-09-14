# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 二叉树最大路径
# @param root TreeNode类
# @return int整型
#
class Solution:
    def maxPathSum(self , root ):
        # write code here

        self.res = float('-inf')

        def dfs(root):

            # 递归：先写结束条件
            if root is None:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)

            left = max(0, left)
            right = max(0, right)
            self.res = max(self.res, left + right + root.val)
            return max(left, right) + root.val

        dfs(root)
        return self.res