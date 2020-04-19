# 输入一个字符串，打印出该字符串中字符的所有排列。
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]


# 回溯法：确定好结束条件，并且规定好第一步，后面的每一步都是递归的过程
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        c, res = list(s), []

        def dfs(x):
            # 递归：先确定结束条件
            if x == len(c) -1:
                res.append("".join(c))
                return
            dic = set()
            for i in range(x, len(c)):
                if c[i] in dic:  # 重复，由此剪枝
                    continue
                dic.add(c[i])
                # print(dic)
                c[i], c[x] = c[x], c[i]
                dfs(x+1)
                c[i], c[x] = c[x], c[i]
                # print('ss')

        dfs(0)
        return list(set(res))


if __name__ == '__main__':
    ob = Solution()
    print(ob.permutation("abb"))