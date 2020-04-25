# -*- coding: utf-8 -*-
# @Time : 2020/4/25 4:32 下午
# @Author : ddz

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：运用递归，返回 left、right

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # 递归：先写结束条件
        if root is None or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None and right is None:
            return
        if right is None:
            return left
        if left is None:
            return right

        return root
