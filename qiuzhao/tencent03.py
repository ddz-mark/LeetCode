# -*- coding: utf-8 -*-
# @Time : 2020/9/6 9:36 下午
# @Author : ddz

# -*- coding: utf-8 -*-

def test(words):
    # words = sorted(words)
    print('words', words)
    a = {}
    for i in words:
        if words.count(i) >= 1:
            a[i] = words.count(i)
    print(a)
    print("________")
    d_order = sorted(a.items(), key=lambda x: x[1], reverse=True)


if __name__ == '__main__':
    words = ['abcd', 'abcd', 'abcd', 'abcd',
             '123q',
             '123cb', '123cb', '123cb']
    test(words)

# row, k = map(int, input().split())
#
# words = []  # 创建空列表
# for i in range(row):  # 使用range进行循环次数
#     words.append(input())  # 添加输入的字符串
# words.sort()  # 由于python中的sort()函数排序后就是以字典排序的形式进行排序，则使用sort()函数即可
#
# a = {}
# for i in words:
#     if words.count(i) >= 1:
#         a[i] = words.count(i)
# # print (a)
#
# print("________")
# d_order = sorted(a.items(), key=lambda x: x[1], reverse=True)
# print(d_order)
# '''
# count=0
# for i,j in d_order:
#     print(i,j)
#     count+=1
#     if count>=k:
#         break
# '''
# b = [0] * len(a)
# for i, j in d_order:
#     b[j] += 1
#
# '''
# d_order=sorted(a.items(),key=lambda x:x[1],reverse=False)
# count=0
# for i,j in d_order:
#     print(i,j)
#     count+=1
#     if count>=k:
#         break
# '''
# '''
# 9 2
# abcd
# abcd
# abcd
# abcd
# 123q
# 123cb
# 123cb
# 123cb
# hurryup
# '''
#
# '''
# 4 2
# 1
# 2
# 3
# 4
# '''
