##
import numpy as np

def test(n, m, a, b):
    res = []
    for i in range(0, n):
        temp = []
        temp_res = []
        for j in range(0, m):
            temp.append((i * j) % 10)

        for j in range(0, m, m - b + 1):
            temp_res.append(max(temp[j:j + b]))

        res.append(temp_res)
    print(res)

    # print(data)
    # for i in range(0, n - a + 1):
    #     line = []
    #     for j in range(0, m, m - b + 1):
    #         line.append(max(data[i:i + a, j:j + b]))
    #     res.extend(line)
    # print(sum(res))


if __name__ == '__main__':
    n, m, a, b = list(map(int, input().split()))
    # n, m, a, b = 3, 4, 3, 3
    test(n, m, a, b)
