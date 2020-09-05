# -*- coding: utf-8 -*-

import sys
def test(s):
    if s == '':
        return ''
    n = len(s)
    s = list(s)
    flag = 0
    for i in range(n - 1, 0, -1):
        if s[i - 1] > s[i]:
            s[i - 1], s[i] = s[i], s[i - 1]
            flag = 1
            break
        else:
            s[i - 1], s[i] = s[i], s[i - 1]

    if flag == 1 and s[0] != '0':
        print("".join(s))
    else:
        print(0)


if __name__ == '__main__':
    # s = sys.stdin.readline().strip()
    # s = '998877665544332211'
    s = '4356'
    test(s)
