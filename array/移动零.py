# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        # 双指针法,遇到0就与后面的快指针换
        i = 0
        for index, num in enumerate(nums):

            if num == 0:
                continue

            if nums[i] == 0:
                nums[i], nums[index] = nums[index], nums[i]

            i += 1

        return nums

        # 遍历，遇到0删除，再在末尾补0
        # for i in nums[:]:
        #     if i==0:
        #         nums.append(0)
        #         nums.remove(0)


if __name__ == '__main__':
    obj = Solution()
    print(obj.moveZeroes([1, 0, 2, 0, 3, 1]))
