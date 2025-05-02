# -*- coding: utf-8 -*-
# @Time : 2025/5/2 22:51
# @Author : ddz
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 思路：逆向双指针
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
