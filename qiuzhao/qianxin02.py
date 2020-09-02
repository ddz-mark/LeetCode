#
#
# @param person int整型一维数组
# @return int整型
#
class Solution:
    def house(self, person):
        # write code here
        n = len(person)
        res = 0
        dp = [1] * n
        if person[1] < person[0]:
            dp[0] = 2
        for i in range(1, n):
            if person[i] > person[i - 1]:
                dp[i] = dp[i - 1] + 1
        print(dp)
        return sum(dp)


if __name__ == '__main__':
    ob = Solution()
    person = [2, 1, 3, 2, 1]
    print(ob.house(person))
