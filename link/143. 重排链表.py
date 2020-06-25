# -*- coding: utf-8 -*-
# @Time : 2020/6/25 2:09 下午
# @Author : ddz
# 181
# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
# 示例 1:
#
# 给定链表 1->2->3->4, 重新排列为 1->4->2->3.
# 示例 2:
#
# 给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    def reverse(self, head):

        new_head = None
        while head:
            pre = head
            head = head.next
            pre.next = new_head
            new_head = pre
        return new_head

    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        # 思路：1. 通过快慢指针确定中位数，然后将后半部分进行反转
        # 2. 进行拼接
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if fast:
            mid = slow.next
        else:
            mid = slow
        # mid = slow

        # 反转链表
        mid = self.reverse(mid)
        new_head = p = ListNode(None)

        i = 0
        while mid:
            if i % 2 == 0:
                p.next = head
                head = head.next
            else:
                p.next = mid
                mid = mid.next
            p = p.next
            i += 1
        if head:
            p.next = head
            head.next = None

        return new_head.next


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
    # node4.next = node5

    new_head = ob.reorderList(node1)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
