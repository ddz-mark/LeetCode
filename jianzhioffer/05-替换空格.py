# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

# 思路一：replace 函数的使用
# 思路二：遍历字符串，使用额外的空间

class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 思路一：
        # return s.replace(" ", "%20")

        # 思路二：
        new_s = ""
        for i in s:
            if i == " ":
                new_s += "%20"
            else:
                new_s += i
        return new_s


if __name__ == '__main__':
    ob = Solution()
    print(ob.replaceSpace("We are happy."))