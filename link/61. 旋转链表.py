# -*- coding: utf-8 -*-
# @Time : 2020/6/24 2:47 下午
# @Author : ddz
# 180

# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 示例 2:
#
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        # 思路：1. 通过快慢指针先确定倒数 第 K 个位置
        # 再通过连接确定
        p = head
        if head is None:
            return None

        length = 0
        while p:
            length += 1
            p = p.next
        if k % length == 0:
            return head

        fast = slow = head
        for _ in range(k % length):
            fast = fast.next
        if fast == head:
            return head

        while fast.next:
            fast = fast.next
            slow = slow.next

        new_head = slow.next
        slow.next = None

        fast.next = head

        return new_head


if __name__ == '__main__':
    ob = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    # node4.next = node5

    new_head = ob.rotateRight(node1, 2)
    while new_head:
        print(new_head.val)
        new_head = new_head.next
