##
##

import collections


def test(n, m, a):
    # 同于定理：判断子数组的和能否被 K 整除就可以写成 (P[j] - P[i-1])%K == 0，根据 同余定理 ，
    # 只要 P[j]%K == P[i-1]%K，就可以保证上面的式子成立。

    p = [0]  # 和数组
    for i in a:
        p.append((p[-1] + i) % m)

    dic = collections.Counter(p)

    print(int(sum(i * (i - 1) / 2 for i in dic.values())))

    ## 暴力解法，超时
    # nums = 0
    # for i in range(0, n):
    #     sum = 0
    #     for j in range(i, n):
    #         sum = sum + a[j]
    #         if sum % m == 0:
    #             nums += 1
    # print(nums)


if __name__ == '__main__':
    # n, m = map(int, input().split())
    # a = list(map(int, input().split()))
    # print(n, m, a)
    test(5, 2, [1, 2, 3, 4, 5])
    # test(n, m, a)
