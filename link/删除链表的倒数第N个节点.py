# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
#
# 示例：
#
# 给定一个链表: 1->2->3->4->5, 和 n = 2.
#
# 当删除了倒数第二个节点后，链表变为 1->2->3->5.
# 说明：
#
# 给定的 n 保证是有效的。


# 思路一：通过遍历先获取链表的长度，然后可以获取倒数 n 的位置，再进行删除。
# 思路二：通过双指针方法，快慢指针相距 n ，快指针达到末尾，则慢指针就是倒数 n，在进行删除。

# Definition for singly-linked list.
class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, node):
        self.head = Node(node)
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

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head = self.head
        slow = fast = head
        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            print('ss')
            print("fast", fast.val)
            print("slow", slow.val)
            fast = fast.next
            slow = slow.next
            print('ss')
            print("fast", fast.val)
            print("slow", slow.val)

        slow.next = slow.next.next

        return head


if __name__ == '__main__':
    node1 = Node(5)
    node2 = Node(6)
    node3 = Node(7)
    linklist = Solution(0)
    linklist.append(node1)
    linklist.append(node2)
    linklist.append(node3)

    # while linklist.head is not None:
    #
    #     print(linklist.head.val)
    #     linklist.head = linklist.head.next

    print(linklist.removeNthFromEnd(linklist.head, 2).val)