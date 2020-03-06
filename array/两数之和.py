# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

class Solution:
    def twoSum(self, nums, target):

        # 解法1：双重遍历
        #         for i, inum in enumerate(nums):
        #             for j, jnum in enumerate(nums[i+1:]):

        #                 if (inum + jnum) == target:
        #                     return [i,i+j+1]

        # 解法2：hash 解法
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i != j:
                return [i, j]
