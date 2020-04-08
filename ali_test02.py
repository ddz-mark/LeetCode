import sys

# 类似于机器人的运动范围，只是唯一变的是mask和步长

def judge(n, k, i, j, matrix, pre_data, flag = 0):
    count1, count2, count3, count4 = 0, 0, 0, 0

    if (0 <= i < n and 0 <= j < n and matrix[i][j] > pre_data):
        for index in range(1, k + 1):
            if flag != 2:
                # 向上走
                count1 += (matrix[i][j] + judge(n, index, i - index, j, matrix,  matrix[i][j], 1))
            if flag != 1:
                # 向下走
                count2 += (matrix[i][j] + judge(n, index, i + index, j, matrix,  matrix[i][j], 2))
            if flag != 4:
                # 向左走
                count3 += (matrix[i][j] + judge(n, index, i, j - index, matrix,  matrix[i][j], 3))
            if flag != 3:
                # 向右走
                count4 += (matrix[i][j] + judge(n, index, i, j + index, matrix,  matrix[i][j], 4))

    return max(count1, count2, count3, count4)


if __name__ == '__main__':
    # print(test(4, [1,3,7,15]))
    # n = int(sys.stdin.readline().strip())
    # a = list(map(int, sys.stdin.readline().strip().split()))
    # print(judge(n, a))

    n, k = 3, 2
    matrix = [[1, 2, 5], [10, 11, 6], [12, 12, 7]]
    print(judge(n, k, 0, 0, matrix, -1))

    print(37)
