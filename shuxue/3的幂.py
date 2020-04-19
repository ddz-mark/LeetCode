# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0 :
            return False

        while n % 3 == 0:
            n /= 3
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    ob = Solution()
    print(ob.isPowerOfThree(9))
