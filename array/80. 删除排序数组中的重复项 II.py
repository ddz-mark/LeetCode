# -*- coding: utf-8 -*-
# @Time : 2020/4/27 12:11 下午
# @Author : ddz

# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 示例 1:
# 给定 nums = [1,1,1,2,2,3],
# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。
# 你不需要考虑数组中超出新长度后面的元素。


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路一：通过删除操作
        # i, count = 1, 1
        # while i < len(nums):
        #
        #     if nums[i - 1] == nums[i]:
        #         count += 1
        #
        #         if count > 2:
        #             nums.pop(i)
        #             i -= 1
        #     else:
        #         count = 1
        #
        #     i += 1
        # return len(nums)

        # 思路二：双指针，移动条件是 < count 就移动 j
        j, count = 1, 1
        for i in range(1, len(nums)):

            if nums[i - 1] == nums[i]:
                count += 1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j += 1

        return j


if __name__ == '__main__':
    ob = Solution()
    print(ob.removeDuplicates([1, 1, 1, 2, 2, 3]))
