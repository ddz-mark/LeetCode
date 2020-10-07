# -*- coding: utf-8 -*-
# @Time : 2020/9/26 8:14 下午
# @Author : ddz

import sys


def test(dic, dic_num, bingfa):

    quene = list()

    i = 0
    pass




if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    values, bingfa = line.split("/")
    print(values, bingfa)

    dic = dict()
    dic_num = dict()
    for v in str(values).split(';'):
        k1, v1, v2 = v.split(':')
        dic[k1] = str(v1[1:-1]).split(',')
        dic_num[k1] = v2
    print(dic)
    print(dic_num)
    test(dic, dic_num, bingfa)
