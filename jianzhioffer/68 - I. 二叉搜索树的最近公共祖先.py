# -*- coding: utf-8 -*-
# @Time : 2020/4/25 11:15 上午
# @Author : ddz

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：最近公共祖先只满足以下条件之一：
# 1. p 和 qq 在 rootroot 的子树中，且分列 rootroot 的 异侧（即分别在左、右子树中）；
# 2. p = root ，且 q 在 root 的左或右子树中；
# 3. q = root ，且 p 在 root 的左或右子树中；


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # 迭代
        # while root:
        #
        #     if root.val > p.val and root.val > q.val:
        #         root = root.left
        #     elif root.val < p.val and root.val < q.val:
        #         root = root.right
        #     else:
        #         break
        #
        # return root

        # 递归
        if root is None:
            return

        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        return root
