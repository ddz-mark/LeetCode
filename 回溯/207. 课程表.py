# -*- coding: utf-8 -*-
# @Time : 2020/6/6 4:31 下午
# @Author : ddz
# 164

# 思路：拓扑排序算法

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 首先根据输入建立 入度表和 邻接表
        indegrees = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]

        # 保存 入度表和邻接表 的数据
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        # 将 入度为0 的节点入队
        depue = list()
        for i, v in enumerate(indegrees):
            if v == 0:
                depue.append(i)

        while depue:
            node = depue.pop(0)
            # 任务数减一
            numCourses -= 1
            for c in adjacency[node]:
                indegrees[c] -= 1  # 入度 - 1
                if indegrees[c] == 0:  # 成为了 0 入度节点就入队
                    depue.append(c)

        return not numCourses


if __name__ == '__main__':
    ob = Solution()
    print(ob.canFinish(2, [[1, 0], [0, 1]]))
