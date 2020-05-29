# -*- coding: utf-8 -*-
# @Time : 2020/5/29 4:58 下午
# @Author : ddz

# 回溯是一种通过穷举所有可能情况来找到所有解的算法

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []
        # 思路：回溯法
        phone = {"2": ["a", "b", "c"],
                 "3": ["d", "e", "f"],
                 "4": ["g", "h", "i"],
                 "5": ["j", "k", "l"],
                 "6": ["m", "n", "o"],
                 "7": ["p", "q", "r", "s"],
                 "8": ["t", "u", "v"],
                 "9": ["w", "x", "y", "z"]
                 }

        res = []

        def dfs(combination, next_digits):

            # 递归：先写结束条件
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for v in phone[next_digits[0]]:
                    dfs(combination + v, next_digits[1:])

        dfs("", digits)

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.letterCombinations(""))
