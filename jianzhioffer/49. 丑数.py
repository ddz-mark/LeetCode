# 我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
#
# 示例:
#
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return n

        uglyNumberList = [1]
        T2, T3, T5 = 0, 0, 0
        for i in range(1, n):

            if uglyNumberList[T2] * 2 <= uglyNumberList[i - 1]:
                T2 += 1
            if uglyNumberList[T3] * 3 <= uglyNumberList[i - 1]:
                T3 += 1
            if uglyNumberList[T5] * 5 <= uglyNumberList[i - 1]:
                T5 += 1
            # print(T2, T3, T5)
            uglyNumberList.append(min(uglyNumberList[T2] * 2, uglyNumberList[T3] * 3, uglyNumberList[T5] * 5))

        return uglyNumberList[-1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.nthUglyNumber(10))
