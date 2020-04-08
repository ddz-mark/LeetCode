# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。

# Definition for a Node.


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """

        # 中序遍历
        # def middle_traverse(root):
        #
        #     # 递归：结束条件
        #     if root is None:
        #         return
        #
        #     front = middle_traverse(root.left)
        #     behind = middle_traverse(root.right)
        #
        #     root.left = front
        #     root.right = behind
        #
        #     if front is not None or behind is not None:
        #         front.right = root
        #         behind.left = root
        #
        #     return root
        #
        # head = root
        # tail = middle_traverse(root)
        # head.left = tail
        # tail.right = head

        # return tail

        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)  # 递归左子树
            self.pre.right, cur.left = cur, self.pre  # 修改引用
            self.pre = cur  # 保存 cur
            dfs(cur.right)  # 递归右子树

        if not root:
            return
        head = self.pre = Node(0)  # 伪头节点
        dfs(root)
        head = head.right  # 去掉伪头节点
        head.left, self.pre.right = self.pre, head
        return head
