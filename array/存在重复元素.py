
# 给定一个整数数组，判断是否存在重复元素。
#
# 如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

class Solution:
    def containsDuplicate(self, nums):

        ## 1. 集合法
        # return len((set(nums))) != len(nums)

        ## 2.排序法
        #         nums.sort()
        # 这里的遍历没有最后一位，因此不需要担心 i+1 会越位
        #         for i in range(len(nums)-1):
        #             if nums[i] == nums[i+1]:
        #                 return True

        #         return False


        ## 3.hash表法
        dic = {}
        for num in nums:
            if dic.get(num):
                return True
            dic[num] = 1

        return False