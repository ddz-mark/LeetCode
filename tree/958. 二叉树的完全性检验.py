# -*- coding: utf-8 -*-
# @Time : 2020/6/27 3:00 下午
# @Author : ddz
# 187

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 思路：BFS，通过判断位置的 index 来达到完全性的检验
        # 这里会遍历到叶子节点的空节点，但是位置不变，如果有其中有个节点没有，index最后一位就对应不上 nodes[-1][1] == len(nodes)
        nodes = [(root, 1)]
        i = 0
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))
        return nodes[-1][1] == len(nodes)
