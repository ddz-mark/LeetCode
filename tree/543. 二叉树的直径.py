# -*- coding: utf-8 -*-
# @Time : 2020/7/5 12:13 下午
# @Author : ddz
# 189

# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
# 示例 :
# 给定二叉树
#
#           1
#          / \
#         2   3
#        / \
#       4   5
# 返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#  
# 注意：两结点之间的路径长度是以它们之间边的数目表示。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1

        def depth(root):
            # 递归：先写结束条件
            if root is None:
                return 0

            leftDepth = depth(root.left)
            rightDepth = depth(root.right)
            self.res = max(self.res, leftDepth + rightDepth + 1)

            return max(leftDepth, rightDepth) + 1

        depth(root)
        return self.res - 1
