# # -*- coding: utf-8 -*-
# # @Time : 2025/5/15 11:32
# # @Author : ddz
#
# # 请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
# # 实现 LRUCache 类：
# # LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
# # int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
# # void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
# # 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
# # 示例：
# # 输入
# # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# # 输出
# # [null, null, null, 1, null, -1, null, -1, 3, 4]
#

class DLinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        # 双向链表
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        # 容量，统计是否超过
        self.size = 0

    def addToHead(self, node):
        # 添加到头部
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def removeNode(self, node):
        # 移除节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToHead(self, node):
        # 移动到头部：先移除节点，再添加到头部
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):
        node = self.tail.prev
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        # 思路：哈希表+双向链表
        # 双向链表按照被使用的顺序存储了这些键值对，靠近头部的键值对是最近使用的，而靠近尾部的键值对是最久未使用的。
        # 哈希表即为普通的哈希映射（HashMap），通过缓存数据的键映射到其在双向链表中的位置。
        # get思路：如果不存在，返回-1；如果存在，则 key 对应的节点是最近被使用的节点。
        #         通过哈希表定位到该节点在双向链表中的位置，并将其移动到双向链表的头部，最后返回该节点的值。
        if key not in self.cache:
            return -1
        # 如果 key 存在，先通过哈希表定位，再移到头部
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # put思路：key不存在，头部添加该节点，并将key和node添加到cache，最后判断是否超过容量，超过就移除尾部节点；
        #         key存在，通过哈希表定位，再将对应的节点的值更新为 value，并将该节点移到双向链表的头部
        if key not in self.cache:
            # 如果 key 不存在，创建一个新的节点
            node = DLinkedNode(key, value)
            # 添加进哈希表
            self.cache[key] = node
            # 添加至双向链表的头部
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.removeTail()
                # 删除哈希表中对应的项
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            # 如果 key 存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # 缓存是 {1=1}
    lRUCache.put(2, 2)  # 缓存是 {1=1, 2=2}
    lRUCache.get(1)  # 返回 1
    lRUCache.put(3, 3)  # 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
    lRUCache.get(2)  # 返回 -1 (未找到)
    lRUCache.put(4, 4)  # 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
    lRUCache.get(1)  # 返回 -1 (未找到)
    lRUCache.get(3)  # 返回 3
    lRUCache.get(4)  # 返回 4
