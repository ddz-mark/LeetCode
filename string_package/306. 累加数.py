# -*- coding: utf-8 -*-
# @Time : 2025/6/6 09:57
# @Author : ddz

# 累加数 是一个字符串，组成它的数字可以形成累加序列。
#
# 一个有效的 累加序列 必须 至少 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。
# 给你一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是 累加数 。如果是，返回 true ；否则，返回 false 。
# 说明：累加序列里的数，除数字 0 之外，不会 以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
#
# 示例 1：
#
# 输入："112358"
# 输出：true
# 解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 示例 2：
#
# 输入："199100199"
# 输出：true
# 解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199

class Solution:
    def validate(self, num1: int, num2: int, remaining: str) -> bool:
        if not remaining:
            return True  # 没有剩余字符，说明整个字符串已经验证完毕

        sum_num = num1 + num2
        sum_str = str(sum_num)

        # 检查剩余的字符串是否以sum_str开头
        if not remaining.startswith(sum_str):
            return False

        # 递归验证剩下的部分
        return self.validate(num2, sum_num, remaining[len(sum_str):])

    def isAdditiveNumber(self, num: str) -> bool:

        # 思路：先通过遍历所有的前两个可能的数字组合，然后再对后续的进行累加数的判断
        n = len(num)
        if n < 3:
            return False  # 累加序列至少需要三个数字

        # 尝试所有可能的前两个数字的组合
        for i in range(1, n // 2 + 1):  # 第一个数字的长度不超过n/2
            for j in range(1, (n - i) // 2 + 1):  # 第二个数字的长度不超过剩余部分的一半
                num1_str = num[:i]
                num2_str = num[i:i + j]

                # 特别情况：检查前导零
                if (len(num1_str) > 1 and num1_str[0] == '0') or (len(num2_str) > 1 and num2_str[0] == '0'):
                    continue

                num1 = int(num1_str)
                num2 = int(num2_str)

                # 验证剩余的字符串是否满足累加序列
                if self.validate(num1, num2, num[i + j:]):
                    return True
        return False


if __name__ == '__main__':
    obj = Solution()
    print(obj.isAdditiveNumber("112358"))
    print(obj.isAdditiveNumber("112359"))
