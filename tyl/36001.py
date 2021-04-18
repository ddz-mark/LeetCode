# -*- coding: utf-8 -*-
# @Time : 2021/3/28 下午7:47
# @Author : ddz
import sys
def test01(n, nums):
    res = 0
    for i in range(n):
        for j in range(i):
            res += (nums[i] | nums[j])

    print(res + sum(nums))


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    nums = list(map(int, sys.stdin.readline().strip().split()))
    test01(n, nums)
