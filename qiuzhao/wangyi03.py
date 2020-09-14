# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:52 下午
# @Author : ddz

# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:52 下午
# @Author : ddz

import sys


def test(s):
    res = 0

    dic = {'a': 0, 'b': 1, 'c': 2, 'x': 3, 'y': 4, 'z': 5}

    # 状态序列
    index_list = [-1] + [None] * 63
    flag = 0
    for i, c in enumerate(s):
        if c in dic:
            print(1 << dic[c], flag ^ (1 << dic[c]))
            flag = flag ^ (1 << dic[c])

        if index_list[flag] is None:
            index_list[flag] = i
        else:
            res = max(res, i - index_list[flag])
    print(res)


if __name__ == '__main__':
    s = 'amabc'

    # s = sys.stdin.readline().strip()
    test(s)
