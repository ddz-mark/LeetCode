# -*- coding: utf-8 -*-
# @Time : 2020/9/13 8:03 下午
# @Author : ddz

import sys


def test(list1, start, end, time):
    # print(list1)
    # print(start)
    # print(end)
    # print(time)

    res_cost = float('inf')

    def dfs(start, end, cost, res_cost):
        if start == end:
            return cost

        for v in list1:
            if start == v[0]:
                res_cost = min(res_cost, dfs(v[1], end, cost + v[2], res_cost))


        return res_cost

    res_cost = dfs(start, end, 0, res_cost)
    print(res_cost)

    day, hour = list(str(time).split('/'))
    month, day = list(str(day).split('.'))
    month = int(month)
    day = int(day)
    hour = int(hour)

    hour_t = (res_cost + hour) % 24
    day_t = (res_cost + hour) // 24

    day_end = (day + day_t) % 30
    month_t = (day + day_t) // 30

    print(str(month+month_t) + '.' + str(day_end) + '/' + str(hour_t))


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    n, m = list(map(int, line.split()))
    list1 = []
    for _ in range(m):
        line1 = sys.stdin.readline().strip()
        n1, m1, time1 = list(map(int, line1.split()))
        list1.append([n1, m1, time1])

    start, end, time2 = sys.stdin.readline().strip().split()
    start = int(start)
    end = int(end)
    test(list1, start, end, time2)
