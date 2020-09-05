# -*- coding: utf-8 -*-

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param arr float浮点型一维数组
# @return int整型
#
class Solution:
    def find_best_cut(self, arr):
        # write code here
        def fun(l):

            s = []
            s_sum = s_s = 0
            for i in range(len(l)):
                s_sum += l[i]
                s_s += l[i] * l[i]
                s.append(s_s / (i + 1) - (s_sum / (i + 1)) ** 2)
            return s

        left = fun(arr[:])
        right = fun(arr[::-1])[::-1]
        minV, index = float('inf'), 0
        for i in range(1, len(right)):
            if left[i - 1] + right[i] < minV:
                minV = left[i - 1] + right[i]
                index = i - 1
        return index + 1


if __name__ == '__main__':
    ob = Solution()
    print(ob.find_best_cut([1, 1, 1, 3, 3, 3]))
