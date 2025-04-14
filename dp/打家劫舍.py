# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
# 如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
#
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
#
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。

# 思路：总结规律，遍历数组时，每个位置决定是否偷，将 nums[i-1] 和 nums[i] + nums[i-2] 相比较，保存最大的

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = [nums[0] for _ in range(len(nums))]
        memo[1] = max(nums[:2])
        for i in range(2, len(nums)):
            choice1 = memo[i - 1]
            choice2 = memo[i - 2] + nums[i]
            memo[i] = max(choice1, choice2)
        print(memo)
        return memo[len(nums) - 1]


if __name__ == '__main__':
    ob = Solution()
    print(ob.rob([2, 7, 9, 3, 1]))
