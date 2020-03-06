# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(1, numRows + 1):
            temp = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    temp.append(1)
                else:
                    temp.append(result[i - 2][j-1] + result[i - 2][j])

            result.append(temp)
        return result


if __name__ == '__main__':
    ob = Solution()
    print(ob.generate(2))
