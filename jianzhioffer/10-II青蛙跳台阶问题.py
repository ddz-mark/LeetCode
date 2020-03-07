# 一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
#
# 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

# 思路：第 n 阶无非是通过第 n-1 阶或者 n-2 阶跳上来
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = dict()
        sum[0], sum[1] = 1, 1
        for i in range(2, n + 1):
            sum[i] = sum[i - 1] + sum[i - 2]

        return sum[n] % 1000000007 if sum[n] > 1000000007 else sum[n]


if __name__ == '__main__':
    ob = Solution()
    print(ob.numWays(7))