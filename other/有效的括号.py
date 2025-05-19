# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) % 2 == 1:
            return False

        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for i in s:
            if i in d:
                stack.append(i)
            else:
                # 判断是否匹配，如果没有或者不匹配，则代表失败
                if not stack or d[stack.pop()] != i:
                    return False
        return stack == []


if __name__ == '__main__':
    ob = Solution()
    print(ob.isValid("()[]{}"))
