# -*- coding: utf-8 -*-
# @Time : 2025/5/22 19:41
# @Author : ddz

# 给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
#
# 回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 例如，121 是回文，而 123 不是。
#
#
# 示例 1：
#
# 输入：x = 121
# 输出：true
# 示例 2：
#
# 输入：x = -121
# 输出：false
# 解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3：
#
# 输入：x = 10
# 输出：false
# 解释：从右向左读, 为 01 。因此它不是一个回文数。
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 思路：弹出x的末尾数字digit = x % 10，x = x // 10，对于回文数组，只需要判断前半部分是否等于后半部分即可
        # 时间复杂度O(logn)
        if x < 0 or (x > 0 and x % 10 == 0):
            return False
        y = 0
        while y < x // 10:
            y = y * 10 + x % 10
            x = x // 10
        # 后续的代表奇数位
        return x == y or y == (x // 10)


if __name__ == '__main__':
    obj = Solution()
    print(obj.isPalindrome(121))
