# -*- coding: utf-8 -*-


def test(nums, k):
    n = len(nums)
    nums = sorted(nums)
    total = 0
    start = end = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum < k:
                if sum > total:
                    total = sum
                    start = i
                    end = j

    print(total, start, end)
    if end < n - 1:
        print(total + nums[-1])
    else:
        print(total + nums[start-1])


if __name__ == '__main__':
    test([1, 2, 3, 4, 5], 14)
