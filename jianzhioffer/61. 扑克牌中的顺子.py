# -*- coding: utf-8 -*-
# @Time : 2020/4/22 10:34 下午
# @Author : ddz

# 从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，
# 可以看成任意数字。A 不能视为 14。
#
# 示例 1:
#
# 输入: [1,2,3,4,5]
# 输出: True
#  
# 示例 2:
#
# 输入: [0,0,1,2,5]
# 输出: True

class Solution(object):
    def isStraight(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        a = list(filter(lambda x: x != 0, nums))
        if len(set(a)) != len(a):
            return False

        return True if max(a) - min(a) <= 4 else False


if __name__ == '__main__':
    ob = Solution()
    print(ob.isStraight([0, 0, 1, 2, 5]))
