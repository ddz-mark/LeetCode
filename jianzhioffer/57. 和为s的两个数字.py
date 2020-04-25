class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if nums == []:
            return []

        dic = {}
        for i, v in enumerate(nums):
            dic[v] = i

        for i, v in enumerate(nums):
            j = dic.get(target - v)
            if j and i != j:
                return [v, target-v]


if __name__ == '__main__':
    ob = Solution()
    print(ob.twoSum([2, 7, 11, 15, 11], 9))
