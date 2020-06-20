# 请判断一个链表是否为回文链表。

# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true
# 进阶：
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 思路一：O(n) 时间复杂度和 O(n) 空间复杂度，通过数组存储链表。
# 思路二：使用快慢指针，确定中位数，然后存储一半的进入数组

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def ReverseList(self, head):
        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
            # head = head.next
        return new_head

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True

        # 快慢指针获取中位数
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #  奇数情况取中位数的下位，中位数不需要比较
        if fast:
            slow = slow.next

        # 比较回文链表
        new_head = self.ReverseList(slow)
        while new_head:
            if head.val != new_head.val:
                return False
            head = head.next
            new_head = new_head.next
        return True




