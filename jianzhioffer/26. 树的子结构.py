# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubStructure(self, A, B):
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """

        if B is None:
            return True

        return self.judge(A, B)

    def judge(self, A, B):

        if A.val == B.val:
            return self.isSubStructure(A.left, B.left)