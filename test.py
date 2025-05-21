
import heapq

class ListNode():

    def __init__(self, val, next=None):
        self.val = val
        self.next= next


def test(link_lists):

    min_heap=[]
    dummy = ListNode(-1)
    head = dummy

    # 表头信息入小根堆
    for i, node in enumerate(link_lists):
        if node:
            heapq.heappush(min_heap, [node.val, node])

    while min_heap:
        val, node = heapq.heappop(min_heap)
        head.next = node
        head = head.next
        # 后续值插入
        if node.next:
            heapq.heappush(min_heap, [node.next.val, node.next])

    return dummy.next

