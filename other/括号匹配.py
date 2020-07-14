# -*- coding: utf-8 -*-
# @Time : 2020/7/14 11:16 下午
# @Author : ddz

# 括号匹配，带 * 号

# 思路：创建两个 Stack，遇到 ) 先从 ( 出栈，再从 * 出栈。当 ( 和 * 栈都还有值的时候，需要判断位置
class Solution(object):

    def isValid(self, s):
        """
        :param s:
        :return:
        """
        stack_c, stack_star = [], []

        for i, c in enumerate(s):

            if c == '(':
                stack_c.append(i)
            elif c == '*':
                stack_star.append(i)
            else:
                if not stack_c and not stack_star:
                    return False
                elif stack_c:
                    stack_c.pop()
                else:
                    stack_star.pop()

        #  注意这里保存的是 index，所以可以判断 *( 这种情况
        while stack_c and stack_star:
            if stack_c[-1] > stack_star[-1]:
                return False
            stack_c.pop()
            stack_star.pop()

        return not stack_c


if __name__ == '__main__':
    ob = Solution()
    print(ob.isValid("*("))
