# -*- coding: utf-8 -*-
# @Time : 2020/7/5 3:13 下午
# @Author : ddz
# 190

# 给出一个完全二叉树，求出该树的节点个数。
# 说明：
# 完全二叉树的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
# 并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。
#
# 示例:
#
# 输入:
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
#
# 输出: 6


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 思路一：通过（root, index）来判断，超时
        # nodes = [(root, 1)]
        # i = 0
        # while i < len(nodes):
        #     node, v = nodes[i]
        #     i += 1
        #     if node.left:
        #         nodes.append((node, 2 * v))
        #     else:
        #         return 2 * v -1
        #
        #     if node.right:
        #         nodes.append((node, 2 * v + 1))
        #     else:
        #         return 2 * v
        #
        # return 0

        # 思路二：计算每个节点
        return 1 + self.countNodes(root.right) + self.countNodes(root.left) if root else 0


