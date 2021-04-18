# -*- coding: utf-8 -*-
# @Time : 2021/3/27 下午3:00
# @Author : ddz
# leetcode 原题：1262. 可被三整除的最大和
# https://leetcode-cn.com/problems/greatest-sum-divisible-by-three/solution/shu-xue-dong-tai-gui-hua-san-de-bei-shu-yg372/

import sys

def test01(nums):
    # 3.自底向上-状态机/动态规划
    mods = [0, 0, 0, 0, 0, 0]  # [模3余0、余1、余2的最大和]
    for cur in nums:
        for m in mods[:]:
            # 如果cur模3余1、m模3余1，那么m+cur模3余2
            # 如果cur模3余1、m模3余2，那么m+cur模3余0
            # ...
            mods[(m + cur) % 6] = max(mods[(m + cur) % 6], m + cur)
    print(mods[0] if mods[0] else -1)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    test01(nums)
