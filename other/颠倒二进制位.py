# 颠倒给定的 32 位无符号整数的二进制位。

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # 把十进制n转换为32位无符号的二进制数组成的列表b
        b = list('{:032b}'.format(n))
        print(b)
        # 32位数颠倒顺序
        for i in range(16):
            b[i], b[31 - i] = b[31 - i], b[i]
        # 将列表元素拼接成字符串
        r = int(''.join(b), 2)

        return r


if __name__ == '__main__':
    ob = Solution()
    print(ob.reverseBits(10))
