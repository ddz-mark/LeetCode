# -*- coding: utf-8 -*-
# @Time : 2020/6/20 5:04 下午
# @Author : ddz
# 172

# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。
#
# 你应当保留两个分区中每个节点的初始相对位置。
#
# 示例:
#
# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # 思路：通过两个辅助链表，一个保存小于 x 的节点，一个保存大于 x 的节点，最后拼接，这样相对位置不变

        l, r = ListNode(0), ListNode(0)
        slow, fast = l, r
        while head:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        l.next = fast.next
        r.next = None
        return slow.next
