# 给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

# 思路：先排序，除此之外的其他，就是最大数 + 1

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i, v in enumerate(sorted(nums)):
            if i != v:
                return i
        return max(nums) + 1


if __name__ == '__main__':
    ob = Solution()
    print(ob.missingNumber([1, 0]))
