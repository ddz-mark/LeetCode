import sys

import re


def test(line):
    # 正则表达式解法
    # for i, v in re.compile(r'(([a-zA-Z0-9])\2*)').findall(line):
    #     # print(i, v)
    #     if len(i) > 2:
    #         line = line.replace(i, "")
    # print(line)

    # 快慢指针
    i = j = 0
    while i < len(line):

        j = i
        while line[i] == line[j] and j < len(line):
            j += 1
        if j - i >= 3:
            line = line[:i] + line[j:]
            i -= 2
            if i < 0:
                i = 0
        else:
            i += 1


if __name__ == '__main__':
    # line = sys.stdin.readline().strip()
    # test('aacccd')

    # print(re.compile(r'(([a-zA-Z])\2*)').findall('abbbssa'))

    # gyq 解法
    # strs = input()
    strs = 'aabbbacc'
    i = j = 0
    while i < len(strs):
        j = i
        while j < len(strs) and strs[j] == strs[i]:
            j += 1
        if j - i >= 3:
            strs = strs[:i] + strs[j:]
            i -= 2
            if i < 0:
                i = 0
        else:
            i += 1
    print(strs)
