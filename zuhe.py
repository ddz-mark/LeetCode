# -*- coding: utf-8 -*-
# @Time : 2020/6/29 11:30 下午
# @Author : ddz
import pandas as pd
import numpy as np


def test(data, listA):
    print(listA)
    res = []
    for i in listA:

        if not data[data['w1'] == i].empty:
            print(data[data['w1'] == i])
        print('ssssssss')
        # if i in data['w1'].values.tolist():
        #     for j in data['w1'].values.tolist():
        #         if j == i:

    print(res)


def test1(S):
    # 思路一：递归，单个字母往后加入，每个新字母都是在结果数组的复制下，再加入大小写
    res = [[]]
    for c in S:
        n = len(res)  # 结果长度
        if c.isalpha():  # 是英文单词
            # 对结果进行复制，然后依次加入大小写
            for i in range(n):
                res.append(res[i][:])  # 复制原值
                res[i].append(c.lower())  # 加入小写
                res[n + i].append(c.upper())  # 加入大写
        else:
            for i in range(n):
                res[i].append(c)

    return list(map("".join, res))


if __name__ == '__main__':
    data = {
        'w1': ['西红柿', '西红柿', 'n', '西红柿'],
        'w2': ['番茄', '番茄1', '11', '番茄2'],
        'relation': ['同义', '改写', '近义', '同义']
    }
    df = pd.DataFrame(data)
    test(df, ['西红柿', '炒', '鸡蛋'])
