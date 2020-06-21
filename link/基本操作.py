# -*- coding: utf-8 -*-
# @Time : 2020/6/20 5:51 下午
# @Author : ddz


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    # 方便调试
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

    # 打印链表
    while node1:
        print(node1.val)
        node1 = node1.next
