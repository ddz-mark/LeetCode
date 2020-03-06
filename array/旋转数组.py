
# 给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
#
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
# 要求使用空间复杂度为 O(1) 的 原地 算法。

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        ## 1. 时间复杂度较高为O(Kn)，时间超时
        # size = len(nums)
        # for i in range(k):
        #     temp = nums[size-1]
        #     for j in range(size-1):
        #         nums[size-1-j] = nums[size-2-j]
        #     nums[0] = temp


        ### 2. 重新组合
        # k=k%len(nums)#保证循环次数在0-len(nums)之间
        # nums[:]=nums[len(nums)-k:]+nums[:len(nums)-k]#切割成两块重新组合


        ### 3. 使用 reversed() 倒序处理
        length = len(nums)
        k = k% length
        nums.reverse()
        nums[0:k] = reversed(nums[0:k])
        nums[k:] = reversed(nums[k:])