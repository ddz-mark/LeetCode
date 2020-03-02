# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
#
# 说明:
#
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 示例:
#
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# 输出: [1,2,2,3,5,6]

class Solution(object):

    def sort(self, nums1):

        # 冒泡排序
        for i, _ in enumerate(nums1):
            for j, _ in enumerate(nums1[i + 1:]):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
        print(nums1)

    # 快排
    def quickSort(self, nums1, head, tail):

        if head < tail:
            base = self.division(nums1, head, tail)  # 确定的位置
            self.quickSort(nums1, head, base - 1)    # 之前的位置排序
            self.quickSort(nums1, base + 1, tail)    # 之后的位置排序

    def division(self, nums1, head, tail):
        base = nums1[head]
        while (head < tail):
            while (head < tail) and (nums1[tail] >= base):
                tail -= 1
            nums1[head] = nums1[tail]
            while (head < tail) and (nums1[head] <= base):
                head += 1
            nums1[tail] = nums1[head]

        nums1[head] = base  # 最后一步比较重要
        return head


    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        print(nums1)
        self.sort(nums1)


if __name__ == '__main__':
    ob = Solution()
    ob.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)
