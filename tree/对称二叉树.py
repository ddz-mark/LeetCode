# 给定一个二叉树，检查它是否是镜像对称的。

# 递归处理

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def judge(self, left, right):

        if left is None and right is None:
            return True
        if left is None and right is not None:
            return False
        if left is not None and right is None:
            return False

        if left.val != right.val:
            return False

        return self.judge(left.right, right.left) and self.judge(left.left, right.right)


    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.judge(root.left, root.right)