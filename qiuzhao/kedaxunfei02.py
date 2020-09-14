# -*- coding: utf-8 -*-

import sys
def test(s):

    s = list(s)
    flag = True
    for i in range(len(s)):
        temp = "".join(list(map(str, s[:i] + s[i+1:])))
        if temp == temp[::-1]:
            flag = False
            print(temp)
            break
    if flag:
        print("false")



if __name__ == '__main__':
    # s = 'abda'
    s = sys.stdin.readline().strip()
    test(s)
