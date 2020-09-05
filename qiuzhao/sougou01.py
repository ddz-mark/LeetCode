# -*- coding: utf-8 -*-


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回能交换奖品的最大数量
# @param a int整型
# @param b int整型
# @param c int整型
# @return int整型
#
class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        res = 0
        l = sorted([a, b, c])
        while True:
            d = min(l)
            res += d
            l = [v - d for v in l]
            # 两位或者三位为 0
            max_n = max(l)
            if max_n <= 1:
                break

            if max_n == sum(l):
                res += max_n // 5
                break
            # 1 位为 0
            else:
                if l[1] == l[2]:
                    res += (l[1] // 2)
                    break
                else:
                    if l[1] != 1:
                        l[0] = l[1] // 2
                        l[1] = l[1] - l[0]
                        l[2] = l[2] - l[0]
                    else:
                        l[0] = 1
                        l[2] -= 2
                    print(l)

        # print(res)
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.numberofprize(1, 1, 9))
