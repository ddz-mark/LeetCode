# -*- coding: utf-8 -*-
# @Time : 2025/5/18 22:28
# @Author : ddz

# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
# 示例 1：
#
# 输入：x = 4
# 输出：2
# 示例 2：
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

class Solution:
    def mySqrt(self, x: int) -> int:
        # 二分法：判断mid^2是否小于等于 x
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.mySqrt(8))
