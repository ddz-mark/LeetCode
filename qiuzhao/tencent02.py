# -*- coding: utf-8 -*-


# 第二题
def test(nums):
    index_set = set()
    exist_list = []
    for i, l in enumerate(nums):
        if i not in exist_list and 0 in list(l):
            index_set = index_set.union(set(l))
            exist_list.append(i)
            # index_set = (set(l))
    print(exist_list)

    for _ in nums:
        for i, l in enumerate(nums):
            if i not in exist_list and index_set.intersection(set(l)):
                index_set = index_set.union(set(l))
                exist_list.append(i)
    print(index_set, len(index_set))


if __name__ == '__main__':
    test([[2, 3],
          [10, 11, 12, 13, 14],
          [0, 1],
          [1, 2],
          [3, 5],
          [6, 7, 8, 2]])
