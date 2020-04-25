# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。
#
# 示例 1：
#
# 输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
# 示例 2：
#
# 输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2]

import collections


class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 思路一：
        # res = []
        # for i, v in collections.Counter(nums).items():
        #     if v == 1:
        #         res.append(i)
        # return res

        # 思路二：
        # 1. 根据全组异或，相同的数异或为0，则一定存在两位不同的数进行异或，得到结果
        # 2. 获取结果的第一位为 1 的位数，（1代表两者不同）
        # 3. 根据这位数进行分组，相同的数一定在同一组，两位不同的数分别在两组。
        ret = 0
        for v in nums:
            ret = ret ^ v  # 异或

        h = 1
        while (ret & h == 0):
            h <<= 1

        a = b = 0
        for n in nums:
            # 根据该位是否为0将其分为两组
            if (h & n == 0):
                a ^= n
            else:
                b ^= n

        return [a, b]


if __name__ == '__main__':
    ob = Solution()
    print(ob.singleNumbers([1, 2, 10, 4, 1, 4, 3, 3]))
