# -*- coding: utf-8 -*-
# @Time : 2020/9/12 1:35 下午
# @Author : ddz

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 最长不重复子串
# @param s string字符串 字符串
# @return int整型
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        # write code here

        record_dic = {}
        j = -1
        count = 0
        length = len(s)
        for i in range(length):
            if s[i] in record_dic:
                j = max(record_dic[s[i]], j)
            record_dic[s[i]] = i
            print(record_dic)
            count = max(count, i - j)

        return count


if __name__ == '__main__':
    ob = Solution()
    print(ob.lengthOfLongestSubstring("zasdwzshda"))
