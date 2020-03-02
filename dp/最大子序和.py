# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。

# 思路 1：对于每个元素，比较之前的最大值和当前元素的和

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 思路一
        # if len(nums) == 0:
        #     return 0
        #
        # current_sum = all_sum = nums[0]
        # for i in range(1, len(nums)):
        #     current_sum = max(current_sum + nums[i], nums[i])
        #     all_sum = max(all_sum, current_sum)
        #
        # return all_sum

        # 思路二
        length = len(nums)
        for i in range(1, length):
            # 当前值的大小与前面的值之和比较，若当前值更大，则取当前值，舍弃前面的值之和
            subMaxSum = max(nums[i] + nums[i - 1], nums[i])
            print('subMaxSum', subMaxSum)
            nums[i] = subMaxSum  # 将当前和最大的赋给nums[i]，新的nums存储的为和值
        print(nums)
        return max(nums)


if __name__ == '__main__':
    ob = Solution()
    print(ob.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
