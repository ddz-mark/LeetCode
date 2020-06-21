# -*- coding: utf-8 -*-
# @Time : 2020/6/21 2:41 下午
# @Author : ddz
# 176

# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 进阶：
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 示例：
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7

# 思路：在两数相加的基础上，加上反转链表

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, head):
        """
        反转链表
        :param head:
        :return:
        """
        new_head = None
        while head:
            pre = head
            head = head.next
            pre.next = new_head
            new_head = pre

        return new_head

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1 = self.reverse(l1)
        l2 = self.reverse(l2)

        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next

            s = s // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return self.reverse(dummy.next)


if __name__ == '__main__':
    ob = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    node6 = ListNode(6)
    node7 = ListNode(7)
    node8 = ListNode(8)
    node9 = ListNode(9)
    node6.next = node7
    node7.next = node8
    node8.next = node9

    ob.addTwoNumbers(node1, node6)
