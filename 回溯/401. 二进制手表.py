# -*- coding: utf-8 -*-
# @Time : 2020/5/26 10:30 下午
# @Author : ddz


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num < 0:
            return []
        # 思路一：暴力枚举
        res = []
        for h in range(12):
            for m in range(60):
                if (bin(h).count('1') + bin(m).count('1')) == num:
                    res.append("%d:%02d" % (h, m))

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.readBinaryWatch(1))