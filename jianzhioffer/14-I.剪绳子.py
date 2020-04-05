# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
# 每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]*k[1]*...*k[m] 可能的最大乘积是多少？
# 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

# 动态规划：关键在于 n 长的绳子，会由1+ n-1,2+ n-2,,,组成

class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n in (1, 2):
            return 1
        elif n == 3:
            return 2

        result = [0, 1, 2, 3]
        for i in range(4, n + 1):
            max = 0
            for j in range(1, i // 2 + 1):
                temp = result[j] * result[i - j]
                if temp > max:
                    max = temp
            result.append(max)

        return result[n]


if __name__ == '__main__':
    ob = Solution()
    print(ob.cuttingRope(5))