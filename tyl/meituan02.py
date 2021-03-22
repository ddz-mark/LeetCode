# -*- coding: utf-8 -*-
# @Time : 2021/3/13 下午4:40
# @Author : ddz

import re
import sys
def test02(s):

    num = sorted(list(map(int, re.findall("\d+", s))))
    for v in num:
        print(v)

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    test02(line)
