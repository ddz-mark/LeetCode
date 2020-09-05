# -*- coding: utf-8 -*-


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能创建的房屋数
# @param t int整型 要建的房屋面宽
# @param xa int整型一维数组 已有房屋的值，其中 x0 a0 x1 a1 x2 a2 ... xi ai 就是所有房屋的坐标和房屋面宽。 其中坐标是有序的（由小到大）
# @return int整型
#
class Solution:
    def getHouses(self, t, xa):
        # write code here

        n = len(xa)
        res = 2
        for i in range(2, n, 2):
            a_right = xa[i-2] + (xa[i-1] /2)
            b_left = xa[i] - (xa[i+1] / 2)
            # print(a_right, b_left)
            if b_left - a_right > t:
                res += 2
            elif b_left - a_right == t:
                res += 1

        return res

if __name__ == '__main__':
    ob = Solution()
    print(ob.getHouses(2, [-1, 4, 5, 2]))
