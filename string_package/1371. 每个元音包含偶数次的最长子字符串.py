# -*- coding: utf-8 -*-
# @Time : 2020/10/8 11:51 下午
# @Author : ddz

# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。
#
# 示例 1：
#
# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。

# 思路如下：
# 1. 当前字母是元音时，需要更新status，更新方式是用当前的status异或元音状态。
# 2. 更新pos中每个状态的位置。因为初始化pos时，除了pos[0]，其他都赋值为-1，
#    所以当前状态在pos中的值为-1时，说明这个状态第一次出现，需要我们更新这个状态在pos中的值。
# 3. 如果当前状态在pos中值不是-1，说明这个状态是第二次出现。这个状态第二次出现，
#    说明在两次出现之间的过程的总体状态是00000（目标出现！！！），因为任一状态异或0等于自身，如00001 xor 00000 = 00001，
#    那么这个过程的长度就是可能的最大长度。



class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        dic = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        res, status = 0, 0
        pos = [0] + [-1] * 31

        for i, v in enumerate(s):

            if v in dic:
                # (1 << dic[v]) 表示是二进制00001
                status = status ^ (1 << dic[v])

            if pos[status] == -1:
                pos[status] = i + 1  # 注意是 i+1，第一个字是辅音字母出现问题
            else:
                res = max(res, i + 1 - pos[status])

        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.findTheLongestSubstring("leetcodeisgreat"))
