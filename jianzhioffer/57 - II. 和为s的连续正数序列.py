# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
# 示例 1：
#
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
#
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]

# 思路一：双指针

class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        i, j = 1, 2
        res = []
        while j <= target // 2 + 1:

            cur_sum = sum(list(range(i, j + 1)))
            if cur_sum < target:
                j += 1
            elif cur_sum > target:
                i += 1
            else:
                res.append(list(range(i, j + 1)))
                j += 1
        return res


if __name__ == '__main__':
    ob = Solution()
    print(ob.findContinuousSequence(2))
