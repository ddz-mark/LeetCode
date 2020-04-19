# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 思路：双指针方式

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        head = tail = 0
        res = 1
        while tail < len(s) - 1:
            tail += 1
            if s[tail] not in s[head:tail]:
                res = max(res, tail - head + 1)
            else:
                while s[tail] in s[head:tail]:
                    head += 1
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.lengthOfLongestSubstring("bbbbbbb"))
