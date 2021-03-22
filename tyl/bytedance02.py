# -*- coding: utf-8 -*-
# @Time : 2021/3/14 上午9:52
# @Author : ddz
import sys

def test02(dic: dict, virus):
    new_virus = []
    for x in virus:
        for k, v in dic.items():
            if x in v:
                new_virus.append(k)

    # 递归：先写结束条件
    if len(set(new_virus)) == 1:
        return new_virus[0]
    elif 0 in new_virus:
        return 0
    else:
        return test02(dic, new_virus)


if __name__ == '__main__':

    # n, m
    n, r = list(map(int, sys.stdin.readline().strip().split()))

    virus = list(map(int, sys.stdin.readline().strip().split()))[1:]
    dic = {}
    for i in range(r):
        # 读取每一行
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        dic[values[0]] = values[2:]

    print(test02(dic, virus))

# 4 2
# 2 2 3
# 0 2 1 2
# 1 1 3
