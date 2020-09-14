# -*- coding: utf-8 -*-
# @Time : 2020/9/9 2:35 下午
# @Author : ddz

import sys

def test(s):
    stack = []
    dic = {'}': '{', ']': '['}
    flag = False
    count = 0
    for c in s:
        if c == '"':
            flag = True
            count += 1
            continue
        if c in dic.values():
            stack.append(c)
            flag = True
        elif c in dic.keys():
            flag = True
            if dic[c] != stack.pop():
                return "false"

    # print(stack, flag, count)
    if flag == False:
        return "true"
    else:
        if count % 2 == 0 and stack == []:
            return "true"
        else:
            return "false"



if __name__ == '__main__':
    # s = '""'
    s = sys.stdin.readline().strip()
    print(test(s))
