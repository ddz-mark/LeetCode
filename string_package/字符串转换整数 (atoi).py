# 说明：
#
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−231,  231 − 1]。如果数值超过这个范围，请返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。
#
# 示例 1:
#
# 输入: "42"
# 输出: 42
# 示例 2:
#
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
#      我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 示例 3:
#
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 示例 4:
#
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
#      因此无法执行有效的转换。
# 示例 5:
#
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
#      因此返回 INT_MIN (−231) 。

INT_MAX = (2 ** 31) -1
INT_MIN = -(2**31)
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0 or (len(str) == 1 and not str[0].isdigit()):
            return 0

        if str[0].isdigit() or str[0] == '-' or str[0] == '+':
            for i, v in enumerate(str):

                if i == 0:
                    continue
                if not v.isdigit():
                    str = str[:i]
                    break
            str_new = 0 if len(str)==1 and (str[0]=='-' or str[0]=='+') else int(str[::])

            if str_new <= -(2 ** 31):
                return INT_MIN
            elif str_new >= INT_MAX:
                return INT_MAX
            else:
                return str_new
        else:
            return 0


if __name__ == '__main__':
    ob = Solution()
    print(ob.myAtoi("-91283472332"))