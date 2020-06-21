# 这个文件主要是写出排序算法

def maopao(nums):
    """
    冒泡排序
    :param nums:
    :return:
    """

    for i in range(len(nums) - 1, 0, -1):
        # print(i)

        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    print(nums)


def quicksort(nums, start, end):
    """
    快速排序
    :param nums:
    :return:
    """
    if start < end:
        base = division(nums, start, end)
        quicksort(nums, start, base - 1)
        quicksort(nums, base + 1, end)


def division(nums, start, end):
    base = nums[start]
    while start < end:
        while base <= nums[end] and start < end:
            end -= 1
        nums[start] = nums[end]

        while base >= nums[start] and start < end:
            start += 1
        nums[end] = nums[start]

    nums[start] = base

    return start


if __name__ == '__main__':
    nums = [3, 1, 4, 6, 8, 4, 2, 5]
    # maopao(nums)
    quicksort(nums, 0, len(nums)-1)
    print(nums)
