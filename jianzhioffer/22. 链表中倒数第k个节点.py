# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。
# 例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
#
# 返回链表 4->5.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, node):
        self.head = ListNode(node)
        self.head.next = None

    def append(self, node):
        """
        链表末尾添加节点
        :param node:
        :return:
        """
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node

    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        fast = slow = head
        for _ in range(0, k):
            print(fast.val)
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        return slow

if __name__ == '__main__':
    node1 = ListNode(5)
    node2 = ListNode(6)
    node3 = ListNode(7)
    linklist = Solution(0)
    linklist.append(node1)
    linklist.append(node2)
    linklist.append(node3)

    linklist.getKthFromEnd(node1, 2)