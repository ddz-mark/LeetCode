# 输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。
#
# 例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

# 示例 1：
#
# 输入：n = 12
# 输出：5
# 示例 2：
#
# 输入：n = 13
# 输出：6


class Solution(object):

    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(1, len(str(n))+1):
            print(i)


if __name__ == '__main__':
    ob = Solution()
    print(ob.countDigitOne(824883294))
