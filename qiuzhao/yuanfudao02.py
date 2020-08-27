# -*- coding: utf-8 -*-
import sys


def maxSubArray(nums):

    length = len(nums)
    for i in range(1, length):
        subMaxSum = max(nums[i] + nums[i - 1], nums[i])
        nums[i] = subMaxSum
    return max(nums)

def test(start_list, end_list):
    n = len(start_list)
    all_list = [[] for i in range(n)]
    res = 0

    for i in range(0, n):
        all_list[i].append(start_list[i])
        for j in range(i + 1, n):
            if end_list[j] - 2 == i:
                all_list[i].append(start_list[j])
    # print(all_list)
    for v in all_list:
        res = max(res, maxSubArray(v))
    print(res)


if __name__ == '__main__':
    # 当输入是单个整数时：
    #
    n = int(input())
    start_list = []
    end_list = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        start_list.append(values[0])
        end_list.append(values[1])

    # start_list = [2, 1, -1]
    # end_list = [0, 2, 2]
    test(start_list, end_list)
