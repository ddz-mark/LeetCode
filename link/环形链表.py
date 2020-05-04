# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

# 思路：快慢指针，如有环，必然相交，无环不相交
# 环形的入口点：设 环长度为 R，交点与入口点的距离是 x
# slow 走的距离是 d = len + x，则 fast 走的距离 2d = len + x + nR，得到 len = nR - x
# 则 len = (n-1)R + R - x，所以只要将 fast 继续走 （R-x）距离，slow 从头开始继续走，第一个相遇点就是环的入口点。
# 代码如下：
# if loopExist == True:
#          slowPtr  = head
#          while slowPtr != fastPtr:
#              fastPtr = fastPtr.next
#              slowPtr = slowPtr.next
#          return slowPtr


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