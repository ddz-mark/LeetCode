# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0:  # 每次递归时，pre都会更新，当pre为0时，说明该节点下面为空。
            return None

        root = TreeNode(preorder[0])
        pos = inorder.index(preorder[0])

        # 中序序列，通过前序找到根节点，左边的是左子树，右边的是右子树。
        # 前序序列，根据中序的值确定
        root.left = self.buildTree(preorder[1:pos + 1], inorder[:pos])
        root.right = self.buildTree(preorder[pos + 1:], inorder[pos + 1:])

        return root
