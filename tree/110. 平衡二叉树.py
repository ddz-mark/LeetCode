# -*- coding: utf-8 -*-
# @Time : 2020/6/27 4:03 下午
# @Author : ddz
# 188

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def depth(self, root):
        """
        # 树的深度
        :param root:
        :return: int
        """

        # 递归：先写结束条件
        if root is None:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) \
               and self.isBalanced(root.right)