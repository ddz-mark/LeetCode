# -*- coding: utf-8 -*-
# @Time : 2025/5/2 22:51
# @Author : ddz
from typing import List


# 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
#
# 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
#
# 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
#
# 示例 1：
#
# 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# 输出：[1,2,2,3,5,6]
# 解释：需要合并 [1,2,3] 和 [2,5,6] 。
# 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。
# 示例 2：
#
# 输入：nums1 = [1], m = 1, nums2 = [], n = 0
# 输出：[1]
# 解释：需要合并 [1] 和 [] 。
# 合并结果是 [1] 。
# 示例 3：
#
# 输入：nums1 = [0], m = 0, nums2 = [1], n = 1
# 输出：[1]
# 解释：需要合并的数组是 [] 和 [1] 。
# 合并结果是 [1] 。
# 注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 思路：正向双指针，比较小的先append，时间复杂度：O(m+n)，空间复杂度：O(m+n)
        # sorted = []
        # p1, p2 = 0, 0
        # while p1 < m or p2 < n:
        #     if p1 == m:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        #     elif p2 == n:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     elif nums1[p1] < nums2[p2]:
        #         sorted.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         sorted.append(nums2[p2])
        #         p2 += 1
        # nums1[:] = sorted

        # 改进思路：逆向双指针，可以避免使用临时变量sorted，
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        while p1 >= 0 or p2 >= 0:
            # 当p1数组结束，全部遍历p2数组
            if p1 == -1:
                nums1[tail] = nums2[p2]
                p2 -= 1
            # 当p2数组结束，全部遍历p1数组
            elif p2 == -1:
                nums1[tail] = nums1[p1]
                p1 -= 1
            # 比较大小
            elif nums1[p1] > nums2[p2]:
                nums1[tail] = nums1[p1]
                p1 -= 1
            else:
                nums1[tail] = nums2[p2]
                p2 -= 1
            tail -= 1


if __name__ == '__main__':
    obj = Solution()
    obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
