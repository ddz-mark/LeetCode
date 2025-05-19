# -*- coding: utf-8 -*-
# @Time : 2025/5/14 20:34
# @Author : ddz
from typing import List


# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
#
# 示例 1：
#
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 示例 2：
#
# 输入：n = 1
# 输出：["()"]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 暴力解法：对于每个位置有"("、")"情况，则一共有2^(2*n)中序列，对每个序列进行括号判断，有效则保留，返回数目即可。
        # def generate(A):
        #     if len(A) == 2 * n:
        #         if valid(A):
        #             ans.append("".join(A))
        #     else:
        #         A.append('(')
        #         generate(A)
        #         A.pop()
        #         A.append(')')
        #         generate(A)
        #         A.pop()
        #
        # def valid(A):
        #     bal = 0
        #     for c in A:
        #         if c == '(':
        #             bal += 1
        #         else:
        #             bal -= 1
        #         if bal < 0: return False
        #     return bal == 0
        #
        # ans = []
        # generate([])
        # return ans

        # 优化方案：只在序列有效时判断继续添加(和)
        # 如果左括号数量不大于 n，我们可以放一个左括号。如果右括号数量小于左括号的数量，我们可以放一个右括号。
        ans = []

        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right + 1)
                S.pop()

        backtrack([], 0, 0)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.generateParenthesis(3))
