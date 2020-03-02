# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）

# Definition for a binary tree node.

# 思路：广度优先遍历
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def _levelOrder(self, level, result, node):
        if node:
            if level == len(result):
                result.append([])

            result[level].append(node.val)
            self._levelOrder(level + 1, result, node.left)
            self._levelOrder(level + 1, result, node.right)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        level, result = 0, list()
        self._levelOrder(level, result, root)
        return result


    # def levelOrder(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: List[List[int]]
    #     """
    #     if root == None:
    #         return []
    #     layer = [root]
    #     res = []
    #     while len(layer):
    #         this_res = []
    #         next_l = []
    #         for n in layer:
    #             this_res.append(n.val)
    #             if n.left:
    #                 next_l.append(n.left)
    #             if n.right:
    #                 next_l.append(n.right)
    #         res.append(this_res)
    #         layer = next_l
    #     return res