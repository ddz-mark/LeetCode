# -*- coding: utf-8 -*-
# @Time : 2020/6/21 1:54 下午
# @Author : ddz
# 175

# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL

# 思路：通过链表的节点操作，可以不用定义空间，只需要定义头节点即可，这里是通过前两个节点当成 奇节点和偶节点

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd_head = head  # 奇数
        even = even_head = head.next  # 偶数
        while odd_head.next and even_head.next:
            odd_head.next = odd_head.next.next
            even_head.next = even_head.next.next

            odd_head, even_head = odd_head.next, even_head.next

        odd_head.next = even
        return head