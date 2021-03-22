# -*- coding: utf-8 -*-
# @Time : 2020/11/25 11:00 上午
# @Author : ddz

# /*
# 现在给你一个数字X，然后让你找一个数M小于等于X，使得M的二进制位数和X的二进制位数一样，且M的二进制
# 中包含1的个数最多，存在多个符合条件的M，请输出最小的M。
# 输入描述：
# 第一行输入一个整数T，代表接下来有T组的测试数据
# 接下来每一行输入一个数n，
# 1 <= n <= 10的1000次方
# 1 <= T <= 10
# 输出描述
# 对于每一组数据，给出一个答案
#
# 示例：
# 输入
# 2
# 12
# 48
#
# 输出
#
# 11
# 47
# */


import sys


def test02(X):
    # 思路：
    # 1. 判断 小于等于 X 的 M，首先确定 X 二进制最高位位数 n
    # 2. 将 n 后面的位数 从右至左 依次补1
    # 3. 判断是否大于等于 X，如果 大于X则返回补1之前的数，如果 等于X则返回X

    n = len(bin(X)) - 3  # 减 3 的原因：bin(X)为0b格式，需要去掉0b
    high = 2 ** n
    # 特殊情况：如 2、4、8
    if high == X:
        return ''
    for i in range(n):  # 从右至左遍历
        if high + (2 ** i) > X:
            return high
        elif high + (2 ** i) == X:
            return X
        else:
            high += 2 ** i


if __name__ == '__main__':
    # X = 48
    X = int(sys.stdin.readline().strip())

    print(test02(X))
