# -*- coding: utf-8 -*-
# @Time : 2020/6/27 2:44 下午
# @Author : ddz
# 186

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # 思路：通过后续最后一位判断根节点，然后通过中序判断左右子树，然后根据左右子树的节点数确定后续的左右节点
        # 递归：先写结束条件
        if len(inorder) == 0:
            return None

        # 确定根节点
        root = TreeNode(postorder[-1])
        pos = inorder.index(postorder[-1])
        # 构建左子树：中序根节点之前、后序（中序根节点直接的节点数）等价于pos
        root.left = self.buildTree(inorder[:pos], postorder[:pos])
        # 构建右子树：中序根节点之后（不包含根节点）、后序是index到倒数第二位（最后一位是根节点）
        root.right = self.buildTree(inorder[pos + 1:], inorder[pos:-1])

        return root
