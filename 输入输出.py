import sys

if __name__ == '__main__':
    # 输入为 [1,2,3,4,5]
    line = eval(sys.stdin.readline().strip())
    print(line)
    print(list(line))

    # 输入为[[1,2],[1,3],[2,4]]
    line = eval(sys.stdin.readline().strip())
    print(line)
    print(list(line))

    # 当输入是单个整数时：
    #
    # n = int(input())
    # 1
    # 当输入的一行有多个整数时，使用split函数将不同的整数分开，将其转为整形，再转为list列表
    #
    # a = list(map(int, input().split()))

    # 当持续有输入且不知道有多少行时，不指定行数， 但是每输入一行就处理一行，持续等待输入
    # import sys
    #
    # for line in sys.stdin:
    #     # a = line.split()
    #     a = list(map(int, line.split()))  # 转为整形列表
    #     print(a[0] + a[1])

    # # 多行输入
    # n = int(sys.stdin.readline().strip())
    # ans = 0
    # for i in range(n):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     for v in values:
    #         ans += v
    # print(ans)

# 工具
# 1. list的交集，并集
# list(set(listA[i + 1:]).intersection(set(listB[:listB.index(listA[i])]))))

# 2. 向下取整、幂函数： math.floor(x / (math.pow(k, i)))

# 3. list 求和 sum函数

# 4. 对字典先按值升序，再按值降序 dict(sorted(dic.items(), key=lambda kv: (kv[1], -kv[0])))

# 5. 词频统计 dic = collections.Counter(p)

# 6. 二维数组转换成一维数组 res = sum(res, [])

# 7. 三角函数：math.sin(math.radians(90))

# 8. 获取二维数组的列：
# a = [[1,2],[3,4]]
# b = list(zip(*a))
# print(b)
# [(1, 3), (2, 4)]

# 对二位数组去重
# list(set([tuple(t) for t in list1]))

# 9. 生成随机数：random.randint(1, 5)
