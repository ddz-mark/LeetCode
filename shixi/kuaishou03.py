import sys


def test(k, n):
    a = [1 for _ in range(k)]
    for i in range(k, n + 1):
        # print("i", i)
        # print(i - k, i)
        a.append(sum(a[i - k:i]))
        # a.append(a[i - 1] + a[i - 2])


    print(a[n] % 397)


if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    k, n = list(map(int, line.split()))

    test(k, n)
    # test(2, 4)
