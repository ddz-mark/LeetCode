# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# 思路：快慢指针，如有换，必然相交，无欢不相交

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast.val == slow.val:
                return True
        return False