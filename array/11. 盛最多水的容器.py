# -*- coding: utf-8 -*-
# @Time : 2020/4/27 3:36 下午
# @Author : ddz

# 思路：双指针，
# 移动短边：如果移动长边，短边值固定，而长度缩小，面积只会越来越小

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 1:
            return 0

        i, j = 0, len(height) - 1
        res = 0
        while i < j:

            if height[i] < height[j]:
                res = max(res, height[i] * (j - i))
                i += 1
            else:
                res = max(res, height[j] * (j - i))
                j -= 1

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
