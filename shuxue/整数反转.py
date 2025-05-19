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
        # 暴力解法：
        # num = 0
        # if x >= 0:
        #     num = int(str(x)[::-1])
        # else:
        #     num = -int(str(-x)[::-1])
        #
        # return num if num >= -(2**31) and num <= 2**31-1 else 0

        # 优化：弹出x的末尾数字digit = x % 10，x = x // 10
        # 弹出的数字加入到y：y = y*10 + digit
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1]，但是取绝对值之后就需要判断 2^31 了
        # 1 << 31 代表左移31位，等于2^31
        boundry = (1 << 31) - 1 if x > 0 else 1 << 31
        while y != 0:
            res = res * 10 + y % 10
            if res > boundry:
                return 0
            y //= 10
        return res if x > 0 else -res

        # 判断是否为回文数组
        # y = 0
        # while x > y:
        #     y = x % 10 + y * 10
        #     x = x // 10
        # return x == y or x == (y // 10)


if __name__ == '__main__':
    ob = Solution()
    print(ob.reverse(1221))
