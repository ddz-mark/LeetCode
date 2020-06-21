# -*- coding: utf-8 -*-
# @Time : 2020/6/21 5:21 下午
# @Author : ddz
# 177

# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 示例 1:
#
# 输入: 1->2->3->3->4->4->5
# 输出: 1->2->5
# 示例 2:
#
# 输入: 1->1->1->2->3
# 输出: 2->3

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 思路：快慢指针确定重复的数据
        if not head:
            return None
        dummy = ListNode(None)
        dummy.next = head

        slow = dummy
        fast = dummy.next

        while fast:
            # 去掉重复数据
            while fast.next and slow.next.val == fast.next.val:
                fast = fast.next

            # 如果 slow 的下位就是 fast，证明无重复数据
            if slow.next == fast:
                slow = fast
            # 有重复数据的时候，需要将 slow 连接到 fast.next 处
            else:
                slow.next = fast.next
            fast = fast.next

        return dummy.next


if __name__ == '__main__':
    ob = Solution()
    node1 = ListNode(2)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    ob.deleteDuplicates(node1)
