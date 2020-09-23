# -*- coding: utf-8 -*-
# @Time : 2020/9/23 10:26 下午
# @Author : ddz

# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。
# 返回二叉搜索树（有可能被更新）的根节点的引用。
#
# 一般来说，删除节点可分为两个步骤：
#
# 首先找到需要删除的节点；
# 如果找到了，删除它。


class Solution:
    def deleteNode(self, root, key):
        if root is None:  # case 0 要删除的节点不存在
            return root
        if root.val > key:  # 要删除的结点在左子树
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:  # 要删除的结点在右子树
            root.right = self.deleteNode(root.right, key)
        else:  # 已经找到了要删除的结点,开始进行删除操作
            # case1 没有孩子,直接删除返回空
            if root.left is None and root.right is None:
                root = None
                return root
            # case2 只有一个孩子,左孩子,让左孩子即位
            elif root.left is not None and root.right is None:
                tmp = root.left
                root = None
                return tmp
            # case3 只有一个孩子,右孩子,让右孩子即位
            elif root.right is not None and root.left is None:
                tmp = root.right
                root = None
                return tmp
            # case4 有两个孩子,和右子树 left most交换后在右子树中删除 left most
            else:
                curr = root.right  # 右子树
                while curr.left:  # find left most
                    curr = curr.left
                # 退出while循环时候的curr就是left most
                root.val = curr.val  # 即位
                root.right = self.deleteNode(root.right, curr.val)  # 在右子树中删除该结点后作为新的右子树
        return root
