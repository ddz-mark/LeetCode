# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
#
# 示例：
#
# 输入：nums = [1,2,3,4]
# 输出：[1,3,2,4]
# 注：[3,1,2,4] 也是正确的答案之一。

# 思路：首尾双指针，停止条件为 头指针大于尾指针

class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # 双指针
        front = 0
        end = len(nums) - 1

        while True:

            print(front, end)
            if front >= end:
                break

            if nums[front] % 2 == 0 and nums[end] % 2 != 0:
                nums[front], nums[end] = nums[end], nums[front]
                front += 1
                end -= 1
            elif nums[front] % 2 != 0 and nums[end] % 2 != 0:
                front += 1
            elif nums[front] % 2 == 0 and nums[end] % 2 == 0:
                end -= 1
            else:
                front += 1
                end -= 1

        return nums


if __name__ == '__main__':
    ob = Solution()
    print(ob.exchange([2, 16, 3, 5, 13, 1, 16, 1, 12, 18, 11, 8, 11, 11, 5, 1]))
    # print(ob.exchange([1,2,3,4]))
