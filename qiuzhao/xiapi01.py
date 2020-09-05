# -*- coding: utf-8 -*-

import sys
import re


def test(s):
    l = []
    l1 = []
    for i, v in enumerate(s):
        if v.isalpha() or v.isalnum():
            l1.append(v)
        else:
            if "".join(l1) != "":
                l.append("".join(l1))
            l1 = []

    if (s[-1].isalpha() or s[-1].isalnum()):
        if "".join(l1) != "":
            l.append("".join(l1))

    res = ''
    for i, v in enumerate(l):
        t = v.lower()
        if i == 0:
            res += t
        else:
            t = list(t)
            t[0] = t[0].upper()
            res += "".join(t)
    print(res)



if __name__ == '__main__':
    # s = 'hello_world'
    # s = 'This is a Demo!'
    # s = '__UPPER__CASE__'
    s = sys.stdin.readline().strip()
    test(s)
