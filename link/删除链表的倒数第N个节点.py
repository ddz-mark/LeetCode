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
from typing import Optional


# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 思路一：通过遍历先获取链表的长度，然后可以获取倒数 n 的位置，再进行删除。
        # 思路二：通过双指针方法，快慢指针相距 n ，快指针达到末尾，则慢指针就是倒数 n，在进行删除。

        # 快慢指针确定位置
        dummy = slow = ListNode(0, head)
        fast = head
        for _ in range(n):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


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
