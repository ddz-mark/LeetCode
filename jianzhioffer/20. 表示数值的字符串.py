# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
# 例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，
# 但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

# 思路：能不能转化为数字就可以了


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except:
            return False

    #     s = s.lower().strip()  # 转化成小写
    #     if (len(s) == 1 and not s[0].isdigit()) or (len(s) == 0):
    #         return False
    #
    #     if len(s.split('e')) == 1:
    #         b, num = self.judge(s)
    #         return b
    #     elif len(s.split('e')) == 2:
    #         s_list = s.split('e')
    #         if s_list[0] == "" or s_list[1] == "":
    #             return False
    #
    #         b1, num1 = self.judge(str(s_list[0]))
    #         b2, num2 = self.judge(str(s_list[1]))
    #
    #         if b1 and b2 and num2 < 1:
    #             return True
    #         else:
    #             return False
    #
    #     else:
    #         return False
    #
    # def judge(self, s):
    #
    #     sign_num = 0
    #     num = 0
    #     if s[0].isdigit() or s[0] == '+' or s[0] == '-' or s[0] == '.':
    #         for i, v in enumerate(s):
    #
    #             if not str(v).isdigit() and str(v) != '.' and str(v) != '+' and str(v) != '-':
    #                 return False, num
    #
    #             if v == '+' or v == '-':
    #                 sign_num += 1
    #             if v == '.':
    #                 num += 1
    #     else:
    #         return False, num
    #
    #     if sign_num > 1 or num > 1:
    #         return False, num
    #
    #     return True, num


if __name__ == '__main__':
    ob = Solution()
    print(ob.isNumber(".1"))
