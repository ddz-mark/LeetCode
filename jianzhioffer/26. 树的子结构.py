# 输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
#
# B是A的子结构， 即 A中有出现和B相同的结构和节点值。

# 思路：先序遍历 + 深度优先遍历


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

        if A is None or B is None:
            return False

        return self.judge(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def judge(self, A, B):
        """
        判断树的节点是否相同
        :param A:
        :param B:
        :return:
        """
        # 递归：结束条件
        if B is None:
            return True
        if A is None:
            return False

        if A.val != B.val:
            return False

        return self.judge(A.left, B.left) and self.judge(A.right, B.right)
