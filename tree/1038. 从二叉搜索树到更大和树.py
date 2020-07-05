# -*- coding: utf-8 -*-
# @Time : 2020/7/5 4:04 下午
# @Author : ddz
# 191

# 给出二叉 搜索 树的根节点，该二叉树的节点值各不相同，修改二叉树，使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
#
# 提醒一下，二叉搜索树满足下列约束条件：
#
# 节点的左子树仅包含键 小于 节点键的节点。
# 节点的右子树仅包含键 大于 节点键的节点。
# 左右子树也必须是二叉搜索树。
#
# 输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 递归解法：中序遍历反向
        # self.num = 0
        # def dfs(root):
        #     # 递归：先写结束条件
        #     if not root:
        #         return
        #
        #     dfs(root.right)
        #     root.val += self.num
        #     self.num = root.val
        #     dfs(root.left)
        #
        # dfs(root)
        # return root

        #  非递归解法
        stack = []
        cur = root
        self.num = 0
        while stack or cur:

            while cur:
                stack.append(cur)
                cur = cur.right

            cur = stack.pop()
            cur.val += self.num
            self.num = cur.val
            cur = cur.left

        return root
