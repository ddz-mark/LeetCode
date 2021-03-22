# -*- coding: utf-8 -*-
# @Time : 2021/3/13 下午5:44
# @Author : ddz



def test03(nums):
    if len(nums) == 1:
        return nums[0]
    numDic = {}
    for i in nums:
        if numDic.has_key(i):
            numDic[i] += 1
            if numDic.get(i) >= (len(nums) + 1) / 2:
                return i
        else:
            numDic[i] = 1


if __name__ == '__main__':
    test03([1,1,2,3])