# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 思路一：运用 stack 的方式进行处理
# 思路二：先求出 链表的长度，然后比较后面的是否相同
# 思路三：使用两个指针 node1，node2 分别指向两个链表 headA，headB 的头结点，然后同时分别逐结点遍历，
# 当 node1 到达链表 headA 的末尾时，重新定位到链表 headB 的头结点；当 node2 到达链表 headB 的末尾时，重新定位到链表 headA 的头结点。
#
class Solution(object):

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 思路一：stack 方式能够得到具体的值
        # stackA = list()
        # stackB = list()
        #
        # pA = headA
        # pB = headB
        # while pA.next:
        #     stackA.append(pA.val)
        #     pA = pA.next
        # while pB.next:
        #     stackB.append(pB.val)
        #     pB = pB.next
        #
        # pre = None
        # while stackA[-1] == stackB[-1]:
        #     pre = stackA.pop()
        #     stackB.pop()
        #
        # return pre

        # 思路二：
        # if headA is None or headB is None:
        #     return None
        #
        # pA = headA
        # pB = headB
        #
        # # 求出长度
        # lengthA = lengthB = 0
        # while pA:
        #     pA = pA.next
        #     lengthA += 1
        # while pB:
        #     pB = pB.next
        #     lengthB += 1
        #
        # if lengthA > lengthB:
        #     longHead = headA
        #     slowHead = headB
        # else:
        #     longHead = headB
        #     slowHead = headA
        #
        # for i in range(abs(lengthB - lengthA)):
        #     longHead = longHead.next
        #
        # while longHead and slowHead and longHead != slowHead:
        #
        #     longHead = longHead.next
        #     slowHead = slowHead.next
        #
        # return longHead

        node1, node2 = headA, headB

        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


if __name__ == '__main__':
    s = Solution()
    pList1Node1 = ListNode(1)
    pList1Node2 = ListNode(2)
    pList1Node3 = ListNode(3)
    pListCommonNode1 = ListNode(6)
    pListCommonNode2 = ListNode(7)
    pList1Node1.next = pList1Node2
    pList1Node2.next = pList1Node3
    pList1Node3.next = pListCommonNode1
    pListCommonNode1.next = pListCommonNode2

    pList2Node1 = ListNode(4)
    pList2Node2 = ListNode(5)
    pList2Node1.next = pList2Node2
    pList2Node2.next = pListCommonNode1
    pListCommonNode1.next = pListCommonNode2

    print(s.getIntersectionNode(pList1Node1, pList2Node1).val)
