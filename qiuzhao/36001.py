# -*- coding: utf-8 -*-
# @Time : 2020/9/11 8:53 下午
# @Author : ddz

import sys

while True:
    s = sys.stdin.readline().strip()
    if not s:
        break

    flag = True

    if len(s) < 8:
        print("Irregular password")
        continue

    cnts = [0, 0, 0, 0]
    for c in s:
        if '0' <= c <= '9':
            cnts[0] = 1
        elif 'a' <= c <= 'z':
            cnts[1] = 1
        elif 'A' <= c <= 'Z':
            cnts[2] = 1
        else:
            cnts[3] = 1

        if sum(cnts) == 4:
            flag = True
        else:
            flag = False

    if flag:
        print("Ok")
    else:
        print("Irregular password")
