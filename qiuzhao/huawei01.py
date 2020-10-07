# -*- coding: utf-8 -*-
# @Time : 2020/9/26 6:57 下午
# @Author : ddz
import sys


def test(performance, organization):
    for k, v in organization.items():
        temp = 0
        for k1, v1 in dict(v).items():
            t = sum([v2 for v2 in v1.values()])
            performance[k1] = t
            temp += t
        performance[k] = temp

    organization_new = dict()
    for k, v in organization.items():
        temp = {}
        for k1, v1 in dict(v).items():
            temp[k1] = dict(sorted(v1.items(), key=lambda kv: (-kv[1], kv[0])))
        organization_new[k] = temp

    organization_new_2 = dict()
    for k, v in organization_new.items():
        organization_new_2[k] = dict(sorted(v.items(), key=lambda kv: (-performance[kv[0]], kv[0])))

    organization_new_3 = dict(sorted(organization_new_2.items(), key=lambda kv: (-performance[kv[0]], kv[0])))

    for k, v in organization_new_3.items():
        print(k + '<' + str(performance[k]) + '>')
        for k1, v1 in dict(v).items():
            print('-' + k1 + '<' + str(performance[k1]) + '>')
            for k2, v2 in v1.items():
                print('--' + k2 + '<' + str(performance[k2]) + '>')


if __name__ == '__main__':

    sys.stdin.readline().strip()

    performance = dict()
    while True:
        line1 = sys.stdin.readline().strip()
        if line1 == "":
            break
        p3, v3 = list(line1.split(','))
        performance[p3] = int(v3)

    sys.stdin.readline().strip()
    organization = dict()
    while True:
        line2 = sys.stdin.readline().strip()
        if line2 == "eof":
            break
        p1, p2, p3 = list(line2.split(','))

        if p1 in organization:
            if p2 in organization[p1]:
                organization[p1][p2][p3] = performance[p3]
            else:
                temp2 = dict()
                temp2[p3] = performance[p3]
                organization[p1][p2] = temp2
        else:
            temp = dict()
            temp1 = dict()
            temp1[p3] = performance[p3]
            temp[p2] = temp1
            organization[p1] = temp
    test(performance, organization)
