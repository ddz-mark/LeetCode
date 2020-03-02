# Definition for singly-linked list.

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def __init__(self, node):
        self.head = Node(node)
        self.head.next = None

    def add(self, node):
        """
        在链表前面添加节点
        :param node:
        :return:
        """
        node.next = self.head.next
        self.head.next = node

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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    node1 = Node(5)
    node2 = Node(6)
    node3 = Node(7)
    linklist = Solution(0)
    linklist.append(node1)
    linklist.append(node2)
    linklist.append(node3)

    while linklist.head is not None:

        print(linklist.head.val)
        linklist.head = linklist.head.next
