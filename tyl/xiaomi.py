# -*- coding: utf-8 -*-
# @Time : 2021/3/3 下午2:44
# @Author : ddz


def test(x):
    str = ''

    while (not (x // 26 == 0 and x % 26 == 0)):

        temp = 25

        if (x % 26 == 0):
            str += chr(temp + 65)
        else:
            str += chr(x % 26 - 1 + 65)

        x //= 26
        # print(str)

    # 倒序输出拼写的字符串
    return str[::-1]

if __name__ == '__main__':
    print(test((703)))
    # print(test1("AAA"))
