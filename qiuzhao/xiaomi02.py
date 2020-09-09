# -*- coding: utf-8 -*-
# @Time : 2020/9/8 7:01 下午
# @Author : ddz

from collections import Counter
def test(l):

    dic = Counter(l)
    d_order = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(d_order[0][1])


if __name__ == '__main__':
    # l = [4, 2, 4, 3]
    n = int(input())
    l = list(map(int, input().split()))
    test(l)
