# -*- coding: utf-8 -*-
# @Time : 2020/9/20 4:13 下午
# @Author : ddz

import sys


def test(ans):
    for v in ans:
        if not str(v).startswith('('):
            print('0')
            continue
        else:
            pass



if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    ans = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        ans.append(line)
    test(ans)
