# -*- coding: utf-8 -*-
# @Time : 2025/6/3 15:32
# @Author : ddz

# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补全和拼写检查。
#
# 请你实现 Trie 类：
#
# Trie() 初始化前缀树对象。
# void insert(String word) 向前缀树中插入字符串 word 。
# boolean search(String word) 如果字符串 word 在前缀树中，返回 true（即，在检索之前已经插入）；否则，返回 false 。
# boolean startsWith(String prefix) 如果之前已经插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。


# 思路：前缀树：使用字符作为节点

class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点字典
        self.is_end = False  # 标记是否是一个单词的结束


class Trie:

    def __init__(self):
        self.root = TrieNode()  # 根节点

    def insert(self, word: str) -> None:
        # 插入思路：如果子节点存在，则一直遍历；如果不存在，创建新的节点
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word: str) -> bool:
        # 搜索思路：一路向下查找，如果中途不存在返回False，查找完查看end状态
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        # 检查是否有单词以给定前缀开头，不需要判断 end 状态
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


if __name__ == '__main__':
    trie = Trie()

    # 插入单词
    words = ["apple", "app", "application", "banana", "ball"]
    for word in words:
        trie.insert(word)

    # 测试搜索
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # True
    print(trie.search("appl"))  # False

    # 测试前缀
    print(trie.startsWith("app"))  # True
    print(trie.startsWith("ban"))  # True
    print(trie.startsWith("cat"))  # False
