# -*- coding: utf-8 -*-
# @Time : 2020/9/23 8:15 下午
# @Author : ddz

import sys


def test(n, line):
    dic = {'J': '11', 'Q': '12', 'K': '13', 'A': '14'}
    dic1 = {'J': '11', 'Q': '12', 'K': '13', 'A': '1'}

    huase = set()
    dianshu = list()
    dianshu1 = list()
    for v in line:
        huase.add(v[0])
        if v[1:] in dic:
            dianshu.append(int(dic[v[1:]]))
            dianshu1.append(int(dic1[v[1:]]))
        else:
            dianshu.append(int(v[1:]))
            dianshu1.append(int(v[1:]))
    dianshu = sorted(dianshu)
    dianshu1 = sorted(dianshu1)

    # 1. 判断同花顺
    count = count1 = 0
    flag = flag1 = False
    i = j = 1
    while i < n:
        while i < n and dianshu[i] - dianshu[i - 1] == 1:
            count += 1
            if count == 4:
                flag = True
                break
            i += 1
        i += 1
    while j < n:
        while j < n and dianshu1[j] - dianshu1[j - 1] == 1:
            count1 += 1
            if count1 == 4:
                flag1 = True
                break
            j += 1
        j += 1

    flag2 = flag or flag1

    # 2. 判断点数
    dic_temp = {}
    for v in dianshu:
        dic_temp[v] = dianshu.count(v)

    if flag2 and len(huase) == 1 and 14 in dianshu:
        print("HuangJiaTongHuaShun")
        return

    if flag2 and len(huase) == 1:
        print('TongHuaShun')
        return

    if 4 in dic_temp.values():
        print('SiTiao')
        return

    if 3 in dic_temp.values() and 2 in dic_temp.values():
        print('HuLu')
        return

    if len(huase) == 1:
        print('TongHua')
        return

    if flag2 and len(huase) > 1:
        print('ShunZi')
        return

    if 3 in dic_temp.values() and 2 not in dic_temp.values():
        print('SanTiao')
        return

    if list(dic_temp.values()).count(2) >= 2:
        print('LiangDui')
        return

    if list(dic_temp.values()).count(2) == 1:
        print('YiDui')
        return
    else:
        print('GaoPai')


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())

    line = sys.stdin.readline().strip().split()

    test(n, line)
