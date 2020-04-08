
import sys
def test(n, nums):
    if n == 0:
        return -1
    min_nums = []
    for i in range(0, n-1):
        min_nums.append(nums[i+1]-nums[i])
    min_nums.append(nums[n-1]-nums[n-2])
    # print(min_nums)

    if min(min_nums)<=0:
        return -1
    for i in min_nums:
        if i % min(min_nums) != 0:
            return -1

    return min(min_nums)

if __name__ == '__main__':
    # print(test(4, [1,3,7,15]))
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().strip().split()))
        print(test(n, a))
