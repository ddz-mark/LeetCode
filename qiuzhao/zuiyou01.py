# -*- coding: utf-8 -*-

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# func getTriggerTime(increase [][]int, requirements [][]int) []int
# @param increase int整型二维数组 属性增加值
# @param requirements int整型二维数组 剧情触发要求
# @return int整型一维数组
#
class Solution:
    def getTriggerTime(self, increase, requirements):
        # write code here

        n = len(increase)
        for i in range(1, n):
            increase[i][0] += increase[i - 1][0]
            increase[i][1] += increase[i - 1][1]
            increase[i][2] += increase[i - 1][2]

        # print(increase)
        res = []
        for r in requirements:
            if r[0] > increase[-1][0] or r[1] > increase[-1][1] or r[2] > increase[-1][2]:
                res.append(-1)
            else:
                for i, v in enumerate(increase):
                    if i == 0:
                        if r[0] <= v[0] and r[1] <= v[1] and r[2] <= v[2]:
                            res.append(i)
                            break
                    else:
                        if r[0] <= v[0] and r[1] <= v[1] and r[2] <= v[2]:
                            res.append(i + 1)
                            break
        return res


if __name__ == '__main__':
    ob = Solution()
    # increase, requirements = [[2, 8, 4], [2, 5, 0], [10, 9, 8]], [[2, 11, 3], [15, 10, 7], [9, 17, 12], [8, 1, 14]]
    # increase, requirements = [[0, 4, 5], [4, 8, 8], [8, 6, 1], [10, 10, 0]], [[12, 11, 16], [20, 2, 6], [9, 2, 6], [10, 18, 3], [8, 14, 9]]
    increase, requirements = [[1, 1, 1]], [[0, 0, 0]]
    print(ob.getTriggerTime(increase, requirements))
