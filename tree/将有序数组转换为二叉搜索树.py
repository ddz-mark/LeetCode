# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
#
# 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def recur(left, right):
            if left > right:
                return None

            # 选择中间位置
            mid = (left + right) // 2

            node = TreeNode(nums[mid])
            node.left = recur(left, mid-1)
            node.right = recur(mid+1, right)
            return node
        return recur(0, len(nums)-1)