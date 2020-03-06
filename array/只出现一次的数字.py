
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
#
# 说明：
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

class Solution:
    def singleNumber(self, nums):

        ## 1. 排序法
        #         nums.sort()
        #         for i in range(0, len(nums)-1, 2):
        #             if nums[i] != nums[i+1]:
        #                 return nums[i]

        #         return nums[-1]

        ## 2. 位运算
        # 异或运算，只要两个相同的数进行异或运算，结果为0；
        # 结合律（即(a^b)^c == a^(b^c)）
        # 交换律 a ^ b = b ^ a
        # 对于任何数x，都有x^x=0，x^0=x
        # 自反性 A XOR B XOR B = A xor 0 = A
        # 那么把这个数组所有数做异或运算，通过交换律和结合律，相同的数抵消，生下来的就是那个不同的数
        # 比如：数组为[a, b, c, a, b]
        # a^b^c^a^b = a^a^b^b^c = (a^a)^(b^b)^c = 0 ^ 0 ^ c = (0 ^ 0) ^ c = 0 ^ c = c

        # sum = 0
        # for i in nums:
        #     sum = sum^i
        # return sum

        ## 3.list的弹出与删除
        while len(nums) != 1:
            lastCha = nums.pop()
            if lastCha in nums:
                nums.remove(lastCha)
            else:
                return lastCha

        return nums[0]