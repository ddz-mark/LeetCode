# -*- coding: utf-8 -*-

import sys
def test03(nums):
    res_sub = []
    res = []
    nums_set = set(nums)

    def dfs_sub(combination, k, candidates):
        # 递归：先写判断条件
        if len(combination) == k and combination[:] not in res_sub and set(combination[:]) == nums_set:
            res_sub.append(combination[:])
            return
        else:
            for v in candidates:
                dfs_sub(combination + [v], k, candidates[candidates.index(v) + 1:])

    for i in range(len(nums) + 1):
        dfs_sub([], i, nums)

    def dfs(x, res_sub_i):
        # 递归：先写结束条件
        if x == len(res_sub_i) - 1:
            temp = int(''.join((str(i) for i in res_sub_i[:])))

            if temp not in res and len(set(str(temp))) == len(nums_set):
                res.append(temp)
        dic = set()
        for i in range(x, len(res_sub_i)):

            # 去重
            if res_sub_i[i] in dic:
                continue
            dic.add(res_sub_i[i])

            res_sub_i[x], res_sub_i[i] = res_sub_i[i], res_sub_i[x]
            dfs(x + 1, res_sub_i)
            # 还原数组，重新进行替换
            res_sub_i[x], res_sub_i[i] = res_sub_i[i], res_sub_i[x]

    for v in res_sub:
        dfs(0, v)
    print(len(res))


if __name__ == '__main__':
    # test03([2, 1,0,1])
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    test03(nums)
