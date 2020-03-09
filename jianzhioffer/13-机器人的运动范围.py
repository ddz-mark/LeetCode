# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
# 它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
# 例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
# 请问该机器人能够到达多少个格子？

# 思路：递归的想法，判断条件就是不能越界，不大于行列之和，重复的格子不增加。


class Solution(object):

    def calbitsum(self, x):
        ressum = 0
        while x != 0:
            ressum += x % 10
            x = x // 10
        return ressum

    def judge(self, m, n, i, j, mask, k):
        count = 0
        if (0 <= i < m and 0 <= j < n and mask[i][j] == False
            and (self.calbitsum(i) + self.calbitsum(j)) <= k):
            mask[i][j] = True
            count = 1 + self.judge(m, n, i - 1, j, mask, k) + \
                    self.judge(m, n, i + 1, j, mask, k) + \
                    self.judge(m, n, i, j - 1, mask, k) + \
                    self.judge(m, n, i, j + 1, mask, k)

        return count

    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        mask = [[False] * n for _ in range(m)]
        if m < 1 or n < 1 or k < 0:
            return 0
        return self.judge(m, n, 0, 0, mask, k)


if __name__ == '__main__':
    ob = Solution()
    print(ob.movingCount(2, 3, 1))

