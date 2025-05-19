# -*- coding: utf-8 -*-
# @Time : 2025/5/18 23:13
# @Author : ddz
import collections
from typing import Optional, List


# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 思路：偶数层倒序： 若 res 的长度为 奇数 ，说明当前是偶数层，则对 tmp 执行 倒序 操作。
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            this_res = []
            next_l = []
            for n in stack:
                this_res.append(n.val)
                if n.left:
                    next_l.append(n.left)
                if n.right:
                    next_l.append(n.right)
            # 关键：执行倒序
            res.append(this_res[::-1] if len(res) % 2 else this_res)
            stack = next_l
        return res
