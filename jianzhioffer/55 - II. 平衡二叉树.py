# 输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路一：自底向上
# 思路二：自顶向下

class Solution(object):

    def depth(self, root):
        if root is None:
            return 0

        return max(self.depth(root.left), self.depth(root.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # 思路一
        # def recur(root):
        #
        #     # 递归：先写结束条件
        #     if root is None:
        #         return 0
        #
        #     left = recur(root.left)
        #     if left == -1:
        #         return -1
        #     right = recur(root.right)
        #     if right == -1:
        #         return -1
        #
        #     return max(left, right) + 1 if abs(left - right) <= 1 else -1
        #
        # return recur(root) != -1

        # 思路二：
        if root is None:
            return True

        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(root.left) and \
               self.isBalanced(root.right)
