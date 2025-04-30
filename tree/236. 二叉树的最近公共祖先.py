# -*- coding: utf-8 -*-
# @Time : 2025/4/30 11:27
# @Author : ddz

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 思路：用递归对二叉树进行先序遍历，遇到p或者q时候返回。
        # 从底回溯到顶，p,q 在root的异侧时候，则返回root为最近公共祖先, 返回root;
        # 如果左右都为空，返回空；否则传递有值的一侧.

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
