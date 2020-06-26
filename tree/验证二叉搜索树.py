# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
#
# 假设一个二叉搜索树具有如下特征：
#
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 思路一：递归处理
# 思路二：中序遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def validBST(self, root, small, large):
        # 递归：结束条件
        if root == None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 思路一
        return self.validBST(root, float('-inf'), float('inf'))

    # 思路二：中序遍历
    # def isValidBST(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: bool
    #     """
    #     stack, inorder = [], float('-inf')
    #
    #     while stack or root:
    #         while root:
    #             stack.append(root)
    #             root = root.left
    #         root = stack.pop()
    #         # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
    #         if root.val <= inorder:
    #             return False
    #         inorder = root.val
    #         root = root.right
    #
    #     return True




