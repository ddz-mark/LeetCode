# -*- coding: utf-8 -*-
# @Time : 2020/10/13 6:32 下午
# @Author : ddz

# 思路：对四个数字进行全排列，之间添加运算符号

def test(n):

    for i in range(n):
        for j in range(0, n-i):
            print(end=" ")
        for k in range(n-i, n):
            print("*", end=" ")
        print(" ")

    for i in range(n):

        for j in range(i):
            print(end=" ")
        for k in range(0, n-i):
            print("*", end=" ")
        print(" ")


def test24(nums):
    s = ['+', '-', '*', '/']

    res = []
    for v in nums:
        # 遍历每个数字之间的运算符
        for s1 in s:
            for s2 in s:
                for s3 in s:

                    # 主要判别括号的操作
                    if (s1 == '+' and s2 == '+' and s3 == '+') or (s1 == '*' and s2 == '*' and s3 == '*'):
                        e = ["{0}{1}{2}{3}{4}{5}{6}".format(v[0], s1, v[1], s2, v[2], s3, v[3])]
                    else:
                        e = ["(({0}{1}{2}){3}{4}){5}{6}".format(v[0], s1, v[1], s2, v[2], s3, v[3]),
                             "({0}{1}{2}){3}({4}{5}{6})".format(v[0], s1, v[1], s2, v[2], s3, v[3]),
                             "({0}{1}({2}{3}{4})){5}{6}".format(v[0], s1, v[1], s2, v[2], s3, v[3]),
                             "{0}{1}{2}{3}{4}{5}{6}".format(v[0], s1, v[1], s2, v[2], s3, v[3])]

                    for e1 in e:
                        if eval(e1) == 24:
                            print('True')
                            exit(-1)

    print('False')

if __name__ == '__main__':
    test(6)
