# -*- coding: utf-8 -*-
# @Time : 2020/4/23 10:21 下午
# @Author : ddz

# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B 中的元素 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。
#
# 示例:
#
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24]


class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        if a == []:
            return []

        b = [1] * len(a)

        for i in range(1, len(a)):
            b[i] = b[i - 1] * a[i - 1]

        temp = 1
        for i in range(len(a) - 2, -1, -1):
            temp = temp * a[i + 1]
            b[i] = b[i] * temp

        return b


if __name__ == '__main__':
    ob = Solution()
    print(ob.constructArr([]))
