# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
#
# 案例:
#
# s = "leetcode"
# 返回
# 0.
#
# s = "loveleetcode",
# 返回
# 2.
#
# 注意事项：您可以假定该字符串只包含小写字母。

# 思路：通过空间换时间，通过两次循环
import collections


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return -1
        # num_dict = dict()
        # for i, v in enumerate(s):
        #     if v in num_dict.keys():
        #         num_dict[v] += 1
        #     else:
        #         num_dict[v] = 1

        num_dict = collections.Counter(s)
        # print(num_dict)

        for i,v in enumerate(s):
            if num_dict[v] == 1:
                return i

        return -1


if __name__ == '__main__':
    ob = Solution()
    print(ob.firstUniqChar("cc"))