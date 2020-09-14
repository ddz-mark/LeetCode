# -*- coding: utf-8 -*-
# @Time : 2020/9/12 1:49 下午
# @Author : ddz

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 向右翻转列表
# @param head ListNode类 listnode 中的头元素
# @param k int整型 向右翻转次数
# @return ListNode类
#
class Solution:
    def rotateRight(self, head, k):
        # write code here
        if head is None:
            return None

        # 确定长度
        length = 0
        p = head
        while p:
            p = p.next
            length += 1

        if k % length == 0:
            return head
        else:

            # 快慢指针
            fast = slow = head
            for _ in range(k % length):
                fast = fast.next

            while fast and fast.next:
                fast = fast.next
                slow = slow.next

            new_head = slow.next
            slow.next = None
            fast.next = head

            return new_head


