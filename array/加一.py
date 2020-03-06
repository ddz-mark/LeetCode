
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。

class Solution:
    def plusOne(self, digits):

        # 解法1：先把数组转换成数字+1，然后在转换成数组
        #         num = 0
        #         i = 1
        #         for d in digits[::-1]:
        #             temp = d * i
        #             i = i * 10
        #             num += temp

        #         num += 1

        #         return map(int,str(num))

        # 解法2：思路一样，只是数组转换成数字的过程使用字符串
        return map(int, str(int(''.join('%s' % i for i in digits) ) +1))