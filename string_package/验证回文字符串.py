# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。
#
# 说明：本题中，我们将空字符串定义为有效的回文串。
#
# 示例 1:
#
# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:
#
# 输入: "race a car"
# 输出: false

# 回文字符串是指正反读都是一样的字符串


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 思路一：双指针
        # front = 0
        # behind = len(s) - 1
        # for i in range(0, behind):
        #
        #     if not str(s[front]).isalnum():
        #         front += 1
        #         continue
        #     if not str(s[behind]).isalnum():
        #         behind -= 1
        #         continue
        #
        #     if front == behind:
        #         break
        #
        #     if not str(s[front]).lower() == str(s[behind]).lower():
        #         return False
        #     else:
        #         front += 1
        #         behind -= 1
        # return True

        # 思路二：先讲除字母和数字的字符串去掉

        new_s = "".join([i for i in s if i.isalnum()]).lower()
        return new_s[::] == new_s[::-1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.isPalindrome("sw"))