# -*- coding: utf-8 -*-
# @Time : 2020/9/12 9:59 上午
# @Author : ddz

import sys


def test(n, nums):
    def dfs(index, target, count):
        count += 1
        if target == index or count >= n:
            return count
        else:
            return dfs(nums[index - 1], target, count)

    count = n + 1
    for i in range(n):
        count = min(count, dfs(nums[i], i + 1, 0))

    print(count)


if __name__ == '__main__':
    # nums = [10, 9, 18, 7]
    n = int(input())

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, line.split()))
    test(n, nums)
