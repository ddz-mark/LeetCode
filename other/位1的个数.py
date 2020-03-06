# 编写一个函数，输入是一个无符号整数，返回其二进制表达式中数字位数为 ‘1’ 的个数（也被称为汉明重量）。

# 思路一：通过 bin 函数先将 10 进制转换成 2 进制，再用 count 函数统计。
# 思路二：通过移位，与 1 进行与操作，如果是1，则count + 1

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 思路一：
        # return bin(n).count('1')

        # 思路二：
        count = 0
        while n != 0:
            if n & 1 == 1:
                count += 1
            n = n >> 1
        return count


if __name__ == '__main__':
    ob = Solution()
    print(ob.hammingWeight(3))
