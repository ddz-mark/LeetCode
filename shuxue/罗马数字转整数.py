# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictory = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)):
            res += dictory[s[i]]
            if 0 < i < len(s) and dictory[s[i - 1]] < dictory[s[i]]:
                res -= 2 * dictory[s[i - 1]]
            else:
                continue
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.romanToInt("MCMXCIV"))