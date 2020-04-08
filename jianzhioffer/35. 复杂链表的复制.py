
# 请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，
# 还有一个 random 指针指向链表中的任意节点或者 null。

# 深拷贝：创造一个对象，不共享内存
# 浅拷贝：复制对象指针，共享内存
# 思路：通过 DFS，用 hash 表存储已经复制的 Node


# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        copy_dict = {}

        def dfs(head):

            # 递归：先写结束条件
            if head is None:
                return None
            if copy_dict.get(head):
                return copy_dict[head]

            copy = Node(head.val, None, None)
            copy_dict[head] = copy
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)

            return copy

        return dfs(head)