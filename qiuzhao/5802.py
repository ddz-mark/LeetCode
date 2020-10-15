# -*- coding: utf-8 -*-
# @Time : 2020/10/11 8:32 下午
# @Author : ddz


#
# 删除重复元素
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def removeDuplicate(self, array):
        # write code here

        n = len(array)

        for i in range(n - 2, -1, -1):
            if array[i] in array[i + 1:]:
                array.pop(i)
        return array

        # l = list(set(array[::-1]))
        # l.sort(key=array[::-1].index)
        # return l[::-1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.removeDuplicate([1,1,1,2,1]))
