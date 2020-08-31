# -*- coding: utf-8 -*-

# 二维数组笛卡尔积

def test(nums):
    rows = len(nums)
    cols = len(nums[0])
    res = []

    def dfs(combines, x):
        # 递归：先写结束条件
        if x == rows:
            res.append(combines[:])
            return

        for i in range(0, cols):
            dfs(combines + [nums[x][i]], x + 1)

    dfs([], 0)
    return res


if __name__ == '__main__':
    nums = [[1, 2, 3],
            [6, 7, 8],
            [11, 12, 13],
            [16, 17, 18]]
    print(test(nums))
