# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL


# 思路一：空间换时间，通过遍历完之后再重新添加。
# 思路二：原地反转，只需要一趟遍历

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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None

        # 思路：cur为当前节点,pre为None节点
        # cur, pre = head, None
        # while cur:
        #     tmp = cur.next
        #     cur.next = pre
        #     # 转移到下一阶段
        #     pre = cur
        #     cur = tmp
        # return pre


        new_head = None
        while head:
            p = head
            head = head.next
            p.next = new_head
            new_head = p
            # head = head.next
        return new_head
