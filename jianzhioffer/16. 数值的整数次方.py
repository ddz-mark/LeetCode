# 实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。
#
# 示例 1:
#
# 输入: 2.00000, 10
# 输出: 1024.00000
# 示例 2:
#
# 输入: 2.10000, 3
# 输出: 9.26100
# 示例 3:
#
# 输入: 2.00000, -2
# 输出: 0.25000
# 解释: 2-2 = 1/22 = 1/4 = 0.25

# 思路一：优化方法，将指数分为奇数和偶数，偶数的话可以 x=x*x
# 判断奇偶的方法：对于(m+n) & 1，若结果为0，则（m+n）是偶数；若结果为1，则（m+n）为奇数；

# 递归思想：可以从后面往前面退，比如：
# 奇数的时候：return x * getPow(x, n-1)
# 偶数的时候：return getPow(x * x, n // 2)

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 1. 迭代版本
        # n_temp = abs(n)
        # sum = 1
        # while n_temp > 1:
        #
        #     if n_temp & 1 == 0:  # 偶数
        #         x = x * x
        #         n_temp = n_temp // 2
        #     else:
        #         sum = sum * x
        #         n_temp -= 1
        # sum = sum * x
        #
        # if n < 0:
        #     return 1 / sum
        # elif n ==0:
        #     return 1
        # return sum

        # 2. 递归版本
        if n == 0:
            return 1
        elif n > 0:
            return self.getPow(x, n)
        else:
            return self.getPow(1/x, -n)

    def getPow(self, x, n):
        # 递归算法，先写结束条件
        if n == 1:
            return x

        if n & 1 == 0:  # 偶数
            return self.getPow(x * x, n // 2)
        else:
            return x * self.getPow(x, n-1)


if __name__ == '__main__':
    ob = Solution()
    print(ob.myPow(2.0, 3))
