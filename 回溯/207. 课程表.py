# -*- coding: utf-8 -*-
# @Time : 2020/6/6 4:31 下午
# @Author : ddz
# 164

# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
# 示例 2：
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

# 思路：拓扑排序算法

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 思路：拓扑排序，建立有向无环图，如果有环则没法排序，排序的目前就是按照无入度的节点先排序的策略，所以排序值并不唯一

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
            # 遍历 入度为0的节点的邻接点，然后将各点的入度值-1，如果入度为0，加入到depue
            for c in adjacency[node]:
                indegrees[c] -= 1  # 入度 - 1
                if indegrees[c] == 0:  # 成为了 0 入度节点就入队
                    depue.append(c)

        return not numCourses


if __name__ == '__main__':
    ob = Solution()
    print(ob.canFinish(2, [[1, 0], [0, 1]]))
