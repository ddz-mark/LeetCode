# -*- coding: utf-8 -*-
# @Time : 2020/4/27 10:57 上午
# @Author : ddz

# 给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。
#
# 函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。
#
# 说明:
#
# 返回的下标值（index1 和 index2）不是从零开始的。
# 你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
# 示例:
#
# 输入: numbers = [2, 7, 11, 15], target = 9
# 输出: [1,2]
# 解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dic = {}
        # for i, v in enumerate(numbers):
        #     dic[v] = i

        # for i, v in enumerate(numbers):
        #     j = dic.get(target - v)
        #     if j and i != j:
        #         return [i + 1, j + 1]
        
        # 双指针法：
        low, high = 0, len(numbers)-1
        while low < high:
            total = numbers[low] + numbers[high]
            if target == total:
                return [low+1, high+1]
            elif target < total:
                high -= 1
            elif target > total:
                low += 1
        return [-1, -1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.twoSum([2, 7, 11, 15], 9))
