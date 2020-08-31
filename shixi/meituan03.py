# 作为一个程序员，修bug（补漏洞）是一项基本的工作。当你刚刚完成一个工作的时候，甲方说你的程序里面有n个bug。
#
# 但是你已经很累了，你希望第一天修x个bug,第二天修[x/k]个bug，第三天修[x/k2]个bug，以此类推，第n天修⌊x/k^(n-1) ⌋个bug，直到修不了bug为止。
#
# [x]的意思是x向下取整。在k大于1的时候，总有一天会修不了一个bug的。所以，你希望在这一天来临之前，修完所有的bug。你要计算，你第一次至少要修多少个bug，即x的最小值为多少。
#
# 输入
# 输入包含一行两个整数n , k 分别代表漏洞总数和题目中的参数k
#
# 输出
# 输出包含一个数，即x的最小值

import math


def test(n, k):
    for x in range(1, n):
        sum = 0
        for i in range(0, n):

            sum += math.floor(x / (math.pow(k, i)))
            # print(sum)
            if sum == n:
                print(x)
                break
        # print("sum", sum)
        # print("x", x)

    # print(x)


if __name__ == '__main__':
    a = list(map(int, input().split()))
    n, k = a[0], a[1]
    test(n, k)
