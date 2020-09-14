#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 编译顺序
# @param input string字符串
# @return string字符串
#

from collections import defaultdict


class Solution:
    def compileSeq(self, input):

        # 处理输入
        input = list(map(int, input[1:len(input) - 1].split(',')))
        inout_new = []
        for i, v in enumerate(input):
            inout_new.append((i, v))

        def dfs(graph, visited, i, combine):
            # 递归：先写结束条件
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True

            visited[i] = 1
            for j in graph[i]:
                if not dfs(graph, visited, j, combine + [j]):
                    return False
            visited[i] = 2
            return True

        # write code here
        graph = defaultdict(list)
        for i, v in inout_new:
            graph[i].append(v)

        print(graph)
        visited = [0] * len(inout_new)
        for i in range(len(inout_new)):
            combine = []
            print(dfs(graph, visited, i, combine))
            # if not dfs(graph, visited, i, []):
            #     return False
        # return True


if __name__ == '__main__':
    ob = Solution()
    input = '"1,2,-1,1"'
    # input = [(0, 1), (1, 2), (2, -1), (3, -1)]
    ob.compileSeq(input)
