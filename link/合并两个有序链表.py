# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
# #
# # 示例：
# #
# # 输入：1->2->4, 1->3->4
# # 输出：1->1->2->3->4->4

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = Node(0)
        new_list = head
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                head.next = l2
                l2 = l2.next
            else:
                head.next = l1
                l1 = l1.next
            head = head.next

        if l2 != None:
            head.next = l2
        elif l1 != None:
            head.next = l1
        return new_list.next
