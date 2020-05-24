# -*- coding: utf-8 -*-
# @Time : 2020/5/24 5:07 下午
# @Author : ddz

# 给定一个元素都是正整数的数组A ，正整数 L 以及 R (L <= R)。
#
# 求连续、非空且其中最大元素满足大于等于L 小于等于R的子数组个数。
#
# 例如 :
# 输入:
# A = [2, 1, 4, 3]
# L = 2
# R = 3
# 输出: 3
# 解释: 满足条件的子数组: [2], [2, 1], [3].


class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        # 思路：通过 <= R 的子数组个数 - <= L-1 的子数组个数
        def count(bound):
            ans = cur = 0
            for v in A:
                # 重点：计算 小于等于 bound 的子数组个数
                # 通过累加的方式，
                cur = cur + 1 if v <= bound else 0
                ans += cur
            return ans

        return count(R) - count(L - 1)


if __name__ == '__main__':
    ob = Solution()
    print(ob.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))
