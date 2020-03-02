# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
#
# 示例 1:
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:
#
# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。
#
# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# 字母异或词意思是字母的长度和字母使用频率一样，但是顺序不对
# 思路：1. 将字符串排序，异或就是一致的
#      2.  使用 Counter 进行统计

import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 思路一
        # return collections.Counter(s) == collections.Counter(t)

        # 思路二
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    ob = Solution()
    print(ob.isAnagram("rat","car"))