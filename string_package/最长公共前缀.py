# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。

# 思路一：通过对字符串使用 min，max。比较最大值与最小值是否一致，如果一致，则中间的一定一致。

# 思路二：api 调用，os.path.commonprefix(list)，返回list中，所有path共有的最长的路径。

import os

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # 思路一：通过对字符串使用 min，max。比较最大值与最小值是否一致，如果一致，则中间的一定一致。
        a = min(strs)
        b = max(strs)

        for i in range(len(a)):
            if a[i] != b[i]:
                return a[:i]
        return a

        # 思路二：
        # return os.path.commonprefix(strs)


if __name__ == '__main__':
    ob = Solution()
    print(ob.longestCommonPrefix(["flower", "flow", "flight"]))
