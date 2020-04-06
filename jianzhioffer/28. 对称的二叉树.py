# 请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root is None:
            return True

        return self.judge(root.left, root.right)

    def judge(self, left, right):

        # 递归：先写结束条件
        if left is None and right is None:
            return True
        elif left is None and right is not None:
            return False
        elif left is not None and right is None:
            return False

        if left.val != right.val:
            return False

        return self.judge(left.left, right.right) and self.judge(left.right, right.left)