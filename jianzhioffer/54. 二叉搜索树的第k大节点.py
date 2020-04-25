# 给定一棵二叉搜索树，请找出其中第k大的节点。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 思路：中序遍历

class Solution(object):

    def midTraverse(self, res, root):
        # 递归：先写结束条件
        if root is None:
            return None

        self.midTraverse(res, root.left)
        res.append(root.val)
        self.midTraverse(res, root.right)

    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = list()
        self.midTraverse(res, root)

        return res[-k]
