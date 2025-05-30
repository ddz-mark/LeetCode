# -*- coding: utf-8 -*-
# @Time : 2025/5/30 10:38
# @Author : ddz

from collections import Counter
import regex as re

corpus = '''low
lower
newest
widest
newest
widest
widest
widest
nice'''

VOVAB_LENGTH = 10


def get_status(corpus):
    # 统计相邻元素 XY出现的频率
    #  找出最大者
    merge_chars = []
    for item in corpus:
        char_list = item.split(' ')
        for i in range(len(char_list) - 1):
            merge_chars.append(''.join(char_list[i:i + 2]))

    chars_count = Counter(merge_chars)
    most_common = chars_count.most_common(1)
    return most_common[0][0]


def merge_chars(corpus, chars_most_common):
    # 和并上一步得到的出现频率最大元素
    for idx, item in enumerate(corpus):
        # 如果chars_most_common=es，\s* 匹配 e 和 s 之间任意数量的空白字符
        # 然后通过re.sub将匹配到的 e 和 s 的子串替换为 es
        corpus[idx] = re.sub('\s*'.join(chars_most_common), chars_most_common, item)
    return corpus


def init(words):
    for idx, word in enumerate((words)):
        words[idx] = ' '.join(list(word)) + ' </w>'
    return words


words = corpus.split('\n')
print("words", words)
corpus = init((words))
print("corpus", corpus)
print("set", set(' '.join(corpus).split(' ')))

while len(set(' '.join(corpus).split(' '))) > VOVAB_LENGTH:
    print("--------------")
    print("corpus", corpus)
    # 找出词频最大的组合
    most_common = get_status(corpus)
    print("most_common", most_common)
    # 合并
    corpus = merge_chars(corpus, most_common)
    print("new_corpus", corpus)
