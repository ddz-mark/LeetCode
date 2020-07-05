# -*- coding: utf-8 -*-
# @Time : 2020/6/26 3:11 下午
# @Author : ddz
# 182

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # 思路一：递归算法
        # if root == []:
        #     return []
        #
        # def recur(root, res):
        #     # 递归：先写结束条件
        #     if root is None:
        #         return None
        #     res.append(root.val)
        #     recur(root.left, res)
        #     recur(root.right, res)
        #
        # res = []
        # recur(root, res)
        # return res

        # 思路二：非递归算法
        if root == []:
            return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                # 这里必须是右子树先入栈
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return res
