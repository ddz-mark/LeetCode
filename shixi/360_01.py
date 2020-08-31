import sys


def test(n, m, nums):
    dic = {}
    i = 0
    for _ in range(len(nums) * m):
        i += 1
        if nums[0] >= nums[1]:
            min_num = nums[1]
            max_num = nums[0]
            position = 1
        else:
            min_num = nums[0]
            max_num = nums[1]
            position = 0

        if dic.get(max_num):
            dic[max_num] += 1
        else:
            dic[min_num] = 0
            dic[max_num] = 1

        if dic.get(max_num) == m:
            print(i)
            break

        nums.pop(position)
        nums.append(min_num)


if __name__ == '__main__':
    # 读取每一行
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    n, m = list(map(int, line.split()))

    # 把每一行的数字分隔后转化成int列表
    nums = list(map(int, sys.stdin.readline().strip().split()))
    # n, m = 4, 3
    # nums = [1, 3, 2, 4]
    test(n, m, nums)
