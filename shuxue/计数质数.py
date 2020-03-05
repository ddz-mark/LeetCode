# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

# 思路一：只能被 1 和 自己整除，但是超时
# 思路二：2 是质数，将所有 2 的倍数置为 非质数

class Solution(object):

    # def judge(self, value):
    #
    #     for i in range(2, value // 2 + 1):
    #         # print("judge", i, value % i)
    #         if value % i == 0:
    #             return False
    #     return True

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路一
        # num = 0
        # for i in range(1, n):
        #     if i == 1:
        #         continue
        #     else:
        #         if self.judge(i):
        #             num += 1
        # return num

        # 思路二
        if n < 3:
            return 0
        arr = [1] * n
        arr[0], arr[1] = 0, 0
        for i in range(2, int(n//2) + 1):
            if arr[i]:
                arr[i*i:n:i] = [0] * ((n - 1) // i - i + 1)
        return sum(arr)


if __name__ == '__main__':
    ob = Solution()
    print(ob.countPrimes(10))
