# 写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：
#
# F(0) = 0,   F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
# 斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 思路：每一项是前两项的和

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = dict()
        sum[0], sum[1] = 0, 1
        for i in range(2, n+1):
            sum[i] = sum[i-1] + sum[i-2]

        return sum[n] % 1000000007 if sum[n] > 1000000007 else sum[n]


if __name__ == '__main__':
    ob = Solution()
    print(ob.fib(45))
