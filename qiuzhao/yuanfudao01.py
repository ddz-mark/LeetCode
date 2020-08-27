# -*- coding: utf-8 -*-
import sys


def test(start_list, end_list):

    n = len(start_list)
    res = 1
    for i in range(0, n):
        for j in range(i+1, n):
            if start_list[j] > start_list[i] and start_list[j] < end_list[i]:
                res += 1
                break
            if start_list[j] <= start_list[i] and end_list[j] > start_list[i]:
                res += 1
                break
    print(res)


if __name__ == '__main__':
    # 当输入是单个整数时：
    #
    n = int(input())
    # start_list = [1, 1, 2, 3]
    # end_list = [4, 2, 3, 4]
    start_list = []
    end_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        start_list.append(values[0])
        end_list.append(values[1])

    test(start_list, end_list)
