# -*- coding: utf-8 -*-
# @Time : 2020/6/20 4:05 下午
# @Author : ddz
# 171

# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def reverse(self, head, tail):

        new_head = tail.next
        p_head = head
        while new_head != tail:
            pre = p_head
            p_head = p_head.next
            pre.next = new_head
            new_head = pre
        return new_head, head

    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # 思路一：通过先确定反转部分的前后节点，分别为 pre, nxt
        if m == n:
            return head

        hair = ListNode(0)
        hair.next = head

        tail = pre = hair
        for i in range(m - 1):
            pre = pre.next

        for i in range(n):
            tail = tail.next

        slow = pre.next
        nxt = tail.next
        r_head, r_tail = self.reverse(slow, tail)
        pre.next = r_head
        r_tail.next = nxt

        return hair.next


if __name__ == '__main__':
    ob = Solution()
    # ob.reverseBetween(1, 2, 4)
    for i in range(4):
        if i >= 2 + 1:
            print('s', i)
        print('a', i)
