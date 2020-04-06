# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 思路：层次遍历

# 先序遍历：
# 先打印根结点，再打印左结点，后打印右结点
#         print(BinaryTreeNode.data)
#         self.preOrder(BinaryTreeNode.left)
#         self.preOrder(BinaryTreeNode.right)

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        level = 0
        self._levelOrder(res, level, root)

        res = sum(res, [])  # 二维数组转换成一维数组
        return res

    def _levelOrder(self, res, level, root):
        if root:
            if level == len(res):
                res.append([])

            res[level].append(root.val)
            self._levelOrder(res, level + 1, root.left)
            self._levelOrder(res, level + 1, root.right)


if __name__ == '__main__':
    res = sum([[2],[1],[3,4]], [])
    print( res)