# -*- coding: utf-8 -*-
# @Time : 2020/6/7 3:25 下午
# @Author : ddz


def test(n, nums):
    # 思路：动态规划
    if n < 3:
        print(1 if sum(nums) == 0 else 0)
    else:
        count = 0
        behind, cur, pre = -1, 0, 1
        # 考虑第一位：
        if nums[0] == 0 and nums[1] == 0:
            nums[0] = 1
            count += 1

        for i in range(1, n - 1):
            # print(i)
            if nums[i + behind] == 0 and nums[i + pre] == 0 and nums[i] == 0:
                nums[i] = 1
                count += 1

        # 考虑最后一位：
        if nums[n - 2] == 0 and nums[n-1] == 0:
            nums[n - 1] = 1
            count += 1
        print(count)


if __name__ == '__main__':
    # 当输入是单个整数时：
    #
    n = int(input())
    nums = list(map(int, input().split()))
    # n = 5
    # nums = [1, 0, 0, 0, 0]
    test(n, nums)
