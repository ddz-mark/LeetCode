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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        # 思路：通过前序判断根节点，然后通过中序判断左右子树，
        # 然后根据中序的index前序的左右子树，比如中序确定左子树有3个节点，那对于前序肯定是根节点之后的3个节点是
        # 递归：先写结束条件
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:pos+1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])

        return root
