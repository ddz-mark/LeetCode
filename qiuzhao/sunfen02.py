# -*- coding: utf-8 -*-
# @Time : 2020/8/29 4:16 下午
# @Author : ddz'

def test(nums):
    length = len(nums)
    for i in range(1, length):
        # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
        subMaxSum = max(nums[i] + nums[i - 1], nums[i])
        print('subMaxSum', subMaxSum)
        nums[i] = subMaxSum  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
    print(nums)
    return max(nums)


if __name__ == '__main__':
    nums = [1, 2, 34]
    test(nums)
