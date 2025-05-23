# -*- coding: utf-8 -*-
# @Time : 2025/5/22 19:59
# @Author : ddz
from typing import Optional


# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。
# 判断该树中是否存在 根节点到叶子节点 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
#
# 叶子节点 是指没有子节点的节点。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # 递归解法
        # if not root:
        #     return False
        # if not root.left and not root.right:
        #     return targetSum == root.val
        # return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)

        # 栈解法
        if not root:
            return False
        stack = []
        stack.append((root, root.val))
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right and path == targetSum:
                return True
            if node.left:
                stack.append((node.left, path + node.left.val))
            if node.right:
                stack.append((node.right, path + node.right.val))
        return False
