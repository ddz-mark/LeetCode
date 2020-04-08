# 输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res, path = [], []

        def recur(root, tar):
            # 递归：结束条件
            if root is None:
                return

            path.append(root.val)
            tar -= root.val

            if tar == 0 and root.left is None and root.right is None:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            # 递归条件下，到达底部删除一个节点
            path.pop()

        recur(root, sum)
        return res
