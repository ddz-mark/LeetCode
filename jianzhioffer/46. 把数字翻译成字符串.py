# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
#
# 示例 1:
#
# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"

# 思路：动态规划，由后向前分析，最后一位翻译存在两种情况：由最后一位组成，由最后两位组成

class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """

        s = str(num)

        a = b = 1

        for i in range(2, len(s) + 1):
            if '10' <= s[i - 2:i] <= '25':
                a, b = a + b, a
            else:
                b = a
            # print('a', a)
        return a


if __name__ == '__main__':
    ob = Solution()
    print(ob.translateNum(12258))
