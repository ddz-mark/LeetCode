# -*- coding: utf-8 -*-
# @Time : 2020/5/13 12:23 下午
# @Author : ddz

# 由 随机数1-5，生成随机数1-7
# 思路：rang5() + (rand5() - 1) * 5 ---> (1,2,3,4,5) + (0, 5, 10, 15, 20)
# 生成等概率的 1-25

import random


def rand5():
    return random.randint(1, 5)


def rand7():
    x = 22
    while (x > 21):
        x = rand5() + (rand5() - 1) * 5

    return 1 + x % 7


if __name__ == '__main__':
    print(rand7())
