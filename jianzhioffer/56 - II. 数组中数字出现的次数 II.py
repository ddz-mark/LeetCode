# 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
#
# 示例 1：
#
# 输入：nums = [3,4,3,3]
# 输出：4
# 示例 2：
#
# 输入：nums = [9,1,7,9,7,9,7]
# 输出：1

import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 思路一：
        # for i, v in collections.Counter(nums).items():
        #     if v == 1:
        #         return i

        # 思路二：
        # 1. 对数组的每位数进行 位求和，若相同数位 1， 则count=3，唯一的不同数为1，count % 3 = 1。
        # 2. 对32位数据进行遍历，这样就得到唯一不同的数的 2 进制数。
        res = 0
        for i in range(32):
            cnt = 0  # 记录当前 bit 有多少个1
            bit = 1 << i  # 记录当前要操作的 bit
            for num in nums:
                if num & bit != 0:
                    cnt += 1
            if cnt % 3 != 0:
                # 不等于0说明唯一出现的数字在这个 bit 上是1
                res |= bit

        return res - 2 ** 32 if res > 2 ** 31 - 1 else res


if __name__ == '__main__':
    ob = Solution()
    print(ob.singleNumber([9, 1, 7, 9, 7, 9, 7]))
