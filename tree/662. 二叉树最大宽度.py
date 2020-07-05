# -*- coding: utf-8 -*-
# @Time : 2020/7/5 4:52 下午
# @Author : ddz
# 192

# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，
# 但一些节点为空。
#
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
#
# 示例 1:
#
# 输入:
#
#            1
#          /   \
#         3     2
#        / \     \
#       5   3     9
#
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        dic = {}

        def dfs(root, level=0, pos=0):
            if root:
                dic.setdefault(level, pos)
                self.res = max(self.res, pos - dic[level] + 1)

                dfs(root.left, level + 1, 2 * pos)
                dfs(root.right, level + 1, 2 * pos + 1)

        dfs(root)
        return self.res
