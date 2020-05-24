# -*- coding: utf-8 -*-
# @Time : 2020/5/24 12:02 下午
# @Author : ddz

# 根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
#
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。
#
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        if T == []:
            return []

        # 思路一：双指针，超时
        # res = [0] * len(T)
        # # 快慢双指针
        # fast = slow = 0
        # while slow < len(T):
        #
        #     while fast < len(T) and T[fast] <= T[slow]:
        #         fast += 1
        #
        #     if fast == len(T):
        #         res[slow] = 0
        #     else:
        #         res[slow] = fast - slow
        #
        #     slow += 1
        #     fast = slow
        #
        # return res

        # 思路二：栈
        ans = [0] * len(T)
        stack = []  # indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans


if __name__ == '__main__':
    ob = Solution()
    print(ob.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
