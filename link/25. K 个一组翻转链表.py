# -*- coding: utf-8 -*-
# @Time : 2020/5/7 9:20 下午
# @Author : ddz

# Definition for singly-linked list.

# 思路：对每 k 个节点进行反转，难点在于怎么与前后链接，所以需要增加之前的指针，和后面的指针



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head, tail):
        new_tail = head
        new_head = None
        tail = tail.next
        while head != tail:
            cur = head
            head = head.next
            cur.next = new_head
            new_head = cur
        return new_head, new_tail

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 思路：1. 先分组，每K个一组. 2. 翻转组内链表，并保存新的头尾指针 3. 再把子链表重新接回原链表

        # 增加头指针，可以防止单独处理
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next
