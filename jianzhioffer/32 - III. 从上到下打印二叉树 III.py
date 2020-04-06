# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，
# 第三行再按照从左到右的顺序打印，其他行以此类推。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        res = []
        level = 0
        self._levelOrder(res, level, root)

        for i, v in enumerate(res):
            if i % 2 == 0:  # 偶数
                res[i] = res[i][::-1]

        return res

    def _levelOrder(self, res, level, root):
        if root:
            if level == len(res):
                res.append([])

            res[level].append(root.val)
            self._levelOrder(res, level + 1, root.left)
            self._levelOrder(res, level + 1, root.right)
