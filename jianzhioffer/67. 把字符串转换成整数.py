# -*- coding: utf-8 -*-
# @Time : 2020/4/25 11:14 上午
# @Author : ddz
INT_MAX = (2 ** 31) -1
INT_MIN = -(2**31)
class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0 or (len(str) == 1 and not str[0].isdigit()):
            return 0

        if str[0].isdigit() or str[0] == '-' or str[0] == '+':
            for i, v in enumerate(str):

                if i == 0:
                    continue
                if not v.isdigit():
                    str = str[:i]
                    break
            str_new = 0 if len(str)==1 and (str[0]=='-' or str[0]=='+') else int(str[::])

            if str_new <= -(2 ** 31):
                return INT_MIN
            elif str_new >= INT_MAX:
                return INT_MAX
            else:
                return str_new
        else:
            return 0