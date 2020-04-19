# 输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
#
# 示例 1:
#
# 输入: [10,2]
# 输出: "102"
# 示例 2:
#
# 输入: [3,30,34,5,9]
# 输出: "3033459"

# 思路：
# 排序判断规则： 设 numsnums 任意两数字的字符串格式 xx 和 yy ，则
# 若拼接字符串 x + y > y + xx+y>y+x ，则 m > nm>n ；
# 反之，若 x + y < y + xx+y<y+x ，则 n < mn<m ；

# 然后按照排序原则，使用快排完成


class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        return "".join([str(i) for i in self.quicksort(nums, 0, len(nums) - 1)])


    def quicksort(self, nums, front, tail):
        # front, tail = 0, len(nums) - 1
        if front < tail:
            base = self.division(nums, front, tail)
            self.quicksort(nums, front, base - 1)
            self.quicksort(nums, base + 1, tail)

        return nums

    def division(self, nums, front, tail):

        base = nums[front]
        # print('base:', base, front, tail)
        while front < tail:
            # 从尾部向前
            while str(base) + str(nums[tail]) <= str(nums[tail]) + str(base) and front < tail:
                tail -= 1
            nums[front] = nums[tail]

            # 从头部先后
            while str(nums[front]) + str(base) <= str(base) + str(nums[front]) and front < tail:
                front += 1
            nums[tail] = nums[front]

        nums[front] = base
        return front


if __name__ == '__main__':
    ob = Solution()
    print(ob.minNumber([3, 30, 34, 5, 9]))
