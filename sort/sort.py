# 这个文件主要是写出排序算法


def insert_sort(L):
    """
    直接插入排序
    :param L:
    :return:
    """
    # 遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    for x in range(1, len(L)):
        # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
        # range(x-1,-1,-1):从x-1倒序循环到0
        for i in range(x - 1, -1, -1):
            # 判断：如果符合条件则交换
            if L[i] > L[i + 1]:
                temp = L[i + 1]
                L[i + 1] = L[i]
                L[i] = temp


def insert_shell(L):
    """
    #希尔排序
    :param L:
    :return:
    """
    # 初始化gap值，此处利用序列长度的一般为其赋值
    gap = (len(L) // 2)
    # 第一层循环：依次改变gap值对列表进行分组
    while (gap >= 1):
        # 下面：利用直接插入排序的思想对分组数据进行排序
        # range(gap,len(L)):从gap开始
        for x in range(gap, len(L)):
            # range(x-gap,-1,-gap):从x-gap开始与选定元素开始倒序比较，每个比较元素之间间隔gap
            for i in range(x - gap, -1, -gap):
                # 如果该组当中两个元素满足交换条件，则进行交换
                if L[i] > L[i + gap]:
                    temp = L[i + gap]
                    L[i + gap] = L[i]
                    L[i] = temp
        # while循环条件折半
        gap = (gap // 2)


def select_sort(L):
    """
    简单选择排序
    :param L:
    :return:
    """
    # 依次遍历序列中的每一个元素
    for x in range(0, len(L)):
        # 将当前位置的元素定义此轮循环当中的最小值
        minimum = L[x]
        # 将该元素与剩下的元素依次比较寻找最小元素
        for i in range(x + 1, len(L)):
            if L[i] < minimum:
                temp = L[i]
                L[i] = minimum
                minimum = temp
        # 将比较后得到的真正的最小值赋值给当前位置
        L[x] = minimum


def heap_sort(elems):
    def siftdown(elems, e, begin, end):  # 向下筛选
        i, j = begin, begin * 2 + 1  # j为i的左子结点
        while j < end:
            if j + 1 < end and elems[j] > elems[j + 1]:  # 如果左子结点大于右子结点
                j += 1  # 则将j指向右子结点
            if e < elems[j]:  # j已经指向两个子结点中较小的位置，
                break  # 如果插入元素e小于j位置的值，则为3者中最小的
            elems[i] = elems[j]  # 能执行到这一步的话，说明j位置元素是三者中最小的，则将其上移到父结点位置
            i, j = j, j * 2 + 1  # 更新i为被上移为父结点的原来的j的位置，更新j为更新后i位置的左子结点
        elems[i] = e  # 如果e已经是某个子树3者中最小的元素，则将其赋给这个子树的父结点
        # 或者位置i已经更新到叶结点位置，则将e赋给这个叶结点。

    # 从最后一个非叶子结点开始，构造大/小根堆
    end = len(elems)
    for i in range(end // 2 - 1, -1, -1):  # 构造堆序。
        siftdown(elems, elems[i], i, end)
    # 进行交换排序
    for i in range((end - 1), 0, -1):  # 进行堆排序.i最后一个值为1，不需要到0
        print(elems)
        e = elems[i]  # 将末尾元素赋给e
        elems[i] = elems[0]  # 交换堆顶与最后一个元素
        siftdown(elems, e, 0, i)

    return (elems)


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
        # 比右边小
        while base <= nums[end] and start < end:
            end -= 1
        nums[start] = nums[end]
        # 比左边大
        while base >= nums[start] and start < end:
            start += 1
        nums[end] = nums[start]
    
    # 最后base赋值
    nums[start] = base

    return start


if __name__ == '__main__':
    nums = [3, 1, 4, 6, 8, 4, 2, 5]
    # maopao(nums)
    quicksort(nums, 0, len(nums) - 1)
    print(nums)
