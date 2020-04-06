# 请完成一个函数，输入一个二叉树，该函数输出它的镜像。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归：先写结束条件
        if root is None:
            return None

        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)

        return root
