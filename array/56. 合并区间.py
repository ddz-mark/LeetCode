# -*- coding: utf-8 -*-
# @Time : 2025/5/23 10:28
# @Author : ddz
from typing import List


# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
#
#
#
# 示例 1：
#
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 示例 2：
#
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # 思路：先按照左端点进行排序，保证子数组从小到大排序
        # 然后，先将第一个子数组保存，后续的每个数组进行判定
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            kv = intervals[i]
            if kv[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(kv[1], res[-1][1])]
            else:
                res.append(kv)

        return res