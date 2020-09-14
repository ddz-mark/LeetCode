# -*- coding: utf-8 -*-
# @Time : 2020/9/12 9:59 上午
# @Author : ddz

import sys


def test(nums):
    avg = sum(nums) / len(nums)
    sum_n = 0
    res = 0
    j = 0
    for i in range(len(nums)):
        sum_n += nums[i]

        if sum_n >= avg * (i - j + 1):
            res += (i - j)
            nums[i] = (sum_n - avg * (i - j))
            j = i
            sum_n = nums[i]

    print(res)


if __name__ == '__main__':
    # nums = [10, 9, 18, 7]
    n = int(input())

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line.split()))
    test(nums)
