# 「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。前五项如下：
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
#
# 给定一个正整数 n（1 ≤ n ≤ 30），输出外观数列的第 n 项。
#
# 注意：整数序列中的每一项将表示为一个字符串。

#思路：只要关注每次更新的规则，通过 count 值来记录是否是重复的数字

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        num = dict()
        num[0] = "1"
        for i in range(0, n):
            num[i+1] = self.bb(num[i])

        return num[n-1]

    def bb(self, n):
        res = []
        count = 0
        for i in range(len(n)):
            if i > 0 and n[i] == n[i - 1]:
                count += 1
                a = str(count) + n[i]
                res[-1] = a
            else:
                count = 1
                a = str(count) + n[i]
                res.append(a)
        return "".join(res)




if __name__ == '__main__':
    ob = Solution()
    print(ob.countAndSay(5))
