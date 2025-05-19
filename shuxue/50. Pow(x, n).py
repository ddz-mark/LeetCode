# -*- coding: utf-8 -*-
# @Time : 2025/5/15 10:42
# @Author : ddz


# 实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，xn ）。
#
# 示例 1：
#
# 输入：x = 2.00000, n = 10
# 输出：1024.00000
# 示例 2：
#
# 输入：x = 2.10000, n = 3
# 输出：9.26100
# 示例 3：
#
# 输入：x = 2.00000, n = -2
# 输出：0.25000
# 解释：2-2 = 1/22 = 1/4 = 0.25


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 思路：递归方案，从右向左推导，如果n为偶数，则x^n=y*y, y=x^(n/2)，如果n为奇数，则x^n=y*y*x
        # def quickMul(N):
        #     if N == 0:
        #         return 1.0
        #     y = quickMul(N // 2)
        #     return y * y if N % 2 == 0 else y * y * x
        #
        # return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

        # 思路：不用递归，使用迭代，注意n为负数的情况
        # 把n次幂拆分为二进制，比如77->(1001101)，则5^77=5^(2^6) * 5^(2^3) * 5^(2^2) * 5^(2^0)
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方, 一直到2进制的第1位
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


if __name__ == '__main__':
    obj = Solution()
    obj.myPow(3, 9)