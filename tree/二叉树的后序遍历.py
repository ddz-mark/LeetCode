# -*- coding: utf-8 -*-
# @Time : 2020/6/26 4:28 下午
# @Author : ddz
# 184

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
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
        #     decur(root.left, res)
        #     decur(root.right, res)
        #     res.append(root.val)
        #
        # res = []
        # recur(root, res)
        # return res

        # 思路二：非递归算法
        # 迭代解法: 跟前序（根左右）是相反的，（根右左），最后再倒序就是（左右根）
        res = []
        stack = []
        cur = root
        while stack or cur:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()

        return res[::-1]   
