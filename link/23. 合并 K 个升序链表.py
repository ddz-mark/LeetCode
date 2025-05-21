# -*- coding: utf-8 -*-
# @Time : 2025/5/21 17:24
# @Author : ddz
from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # 方案一：使用小根堆的思路，时间O(nlogk)、空间O(K)堆中至多有 k 个元素。
        h = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i]]
        heapq.heapify(h)
        dummy = ListNode(-1, None)
        cur = dummy
        while h:
            _, i, node = heapq.heappop(h)
            cur.next = node
            if node.next:
                heapq.heappush(h, (node.next.val, i, node.next))
            cur = cur.next
        return dummy.next

        # 方案二：使用归并排序
        # 思路：两两合并，时间O(nlogk)、空间O(logk)
        # 21. 合并两个有序链表
        # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #     cur = dummy = ListNode()  # 用哨兵节点简化代码逻辑
        #     while list1 and list2:
        #         if list1.val < list2.val:
        #             cur.next = list1  # 把 list1 加到新链表中
        #             list1 = list1.next
        #         else:  # 注：相等的情况加哪个节点都是可以的
        #             cur.next = list2  # 把 list2 加到新链表中
        #             list2 = list2.next
        #         cur = cur.next
        #     cur.next = list1 if list1 else list2  # 拼接剩余链表
        #     return dummy.next

        # def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #     m = len(lists)
        #     if m == 0:
        #         return None
        #     step = 1
        #     while step < m:
        #         for i in range(0, m - step, step * 2):
        #             lists[i] = self.mergeTwoLists(lists[i], lists[i + step])
        #         step *= 2
        #     return lists[0]


if __name__ == '__main__':
    dumpy1 = head1 = ListNode()
    for i in range(1, 3, 5):
        node = ListNode(i)
        head1.next = node
        head1 = head1.next
    dumpy2 = head2 = ListNode()
    for i in range(2, 3, 6):
        node = ListNode(i)
        head2.next = node
        head2 = head2.next
    obj = Solution()
    obj.mergeKLists([dumpy1.next, dumpy2.next])