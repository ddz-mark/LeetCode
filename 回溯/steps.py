# -*- coding: utf-8 -*-
# @Time : 2020/6/29 12:58 下午
# @Author : ddz

# 数组[1,2,3,4]，每次可以走<=3步，也就是结果为[1,2,3,4](每次走1步)、[12,3,4](第一次走2步，第二三次走1步)。。。以此内推


def test(str1):
    res = []

    def dfs(start, step, tmp):
        # 递归：先写结束条件
        tmp.append(str1[start:start + step])
        # 字符串
        # if "".join(tmp) == str1 and tmp not in res:
        #     res.append(tmp)
        # 数组
        if sum(tmp, []) == str1 and tmp not in res:
            res.append(tmp)

        for i in range(1, 4):
            if start + step + i <= len(str1):
                tmp = dfs(start + step, i, tmp)
                tmp = tmp[:-1]

        return tmp

    for i in range(1, 4):
        dfs(0, i, [])
    print('res', len(res), res)


if __name__ == '__main__':
    test([1, 2, 3, 4])
