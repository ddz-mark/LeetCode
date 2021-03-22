# -*- coding: utf-8 -*-
# @Time : 2021/3/21 下午9:31
# @Author : ddz

import sys
def test03(nums, pos):
    for i in range(0, len(nums) - 1):  # 控制比较的轮数
        for j in range(i + 1, len(nums)):  # 控制每轮比较的次数
            if i in pos and nums[i] > nums[j]:
                return "NO"
            if nums[i] < nums[j]:  # 从大到小排列
                nums[i], nums[j] = nums[j], nums[i]  # 利用序列解包交换这两个数的值
    return "YES"


if __name__ == '__main__':
    print(test03(nums=[5, 4, 2, 3, 1], pos=[4]))

    t = int(sys.stdin.readline().strip())
    for i in range(t):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
