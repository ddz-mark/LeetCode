from collections import *


class Solution:
    def intersect(self, nums1, nums2):

        # 普通解法1
        #         result = []
        #         for i in nums1:
        #             if i in nums2:
        #                 result.append(i)
        #                 # remove 删除的是第一个与value值相等的数
        #                 nums2.remove(i)

        #         return result

        # 普通解法2
        # Counter 是用来进行计数的工具
        # return list((Counter(nums1) & Counter(nums2)).elements())

        # 进阶解法1：
        nums1.sort()
        nums2.sort()
        i = j = 0
        result = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return result
