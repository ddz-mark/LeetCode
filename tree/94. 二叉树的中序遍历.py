# -*- coding: utf-8 -*-
# @Time : 2020/6/26 3:42 下午
# @Author : ddz
# 183

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
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
        #
        #     recur(root.left, res)
        #     res.append(root.val)
        #     recur(root.right, res)
        # res = []
        # recur(root, res)
        # return res

        # 思路二：非递归算法
        if root == []:
            return []
        stack, res = [], []
        cur = root
        while stack or cur:
            # 一直往下走，直到最左边的节点
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right

        return res




