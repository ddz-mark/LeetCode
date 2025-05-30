# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
# 解题思路：
# 运用双指针，快指针进行遍历，慢指针与快指针对比，遇到不一样的，则慢指针加1，快指针的值赋值给慢指针更新后的位置，代码如下：

class Solution:
    def removeDuplicates(self, nums):

        i = 0
        for v in nums:
            if nums[i] != v:
                i += 1
                nums[i] = v

        # and中含0，则返回0；都非0，则返回后一个值
        return len(nums) and i + 1


if __name__ == '__main__':
    obj = Solution()
    print(obj.removeDuplicates([1, 2, 3, 3, 4]))
