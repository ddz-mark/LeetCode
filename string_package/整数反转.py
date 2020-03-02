# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
#
# 示例 1:
#
# 输入: 123
# 输出: 321
#  示例 2:
#
# 输入: -123
# 输出: -321
# 示例 3:
#
# 输入: 120
# 输出: 21
# 注意:
#
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# 思路：整数转换为字符串

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        if x >= 0:
            num = int(str(x)[::-1])
        else:
            num = -int(str(-x)[::-1])

        return num if num >= -(2**31) and num <= 2**31-1 else 0


if __name__ == '__main__':
    ob = Solution()
    print(ob.reverse(12))