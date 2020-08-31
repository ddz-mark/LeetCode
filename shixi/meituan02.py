# 输入
# 输入第一行仅包含一个正整数n，表示选手数量。(1<=n<=10^5)
#
# 输入第二行包含n个正整数，是一个1-n的排列A，表示出发顺序，A[i]表示第i个出发的选手的编号。
#
# 输入第三行同样包含一个1-n的排列B，表示到达顺序，B[i]表示第i个到达的选手的编号。
#
# 输出
# 输出仅包含一个整数，表示得到表彰的人数。
#
#
# 样例输入
# 5
# 5 3 1 4 2
# 2 4 5 1 3
# 样例输出
# 3

def test(n, listA, listB):
    res = list()
    for i in range(0, n):
        res.extend(list(set(listA[i + 1:]).intersection(set(listB[:listB.index(listA[i])]))))
        res = list(set(res))
    print(len(res))

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # a, b = [5, 3, 1, 4, 2], [2, 4, 5, 1, 3]
    test(n, a, b)
    # print(a.index(2))
    # print(list(set(a).intersection(set(b))))
    # print(list(set(a).union(set(b))))
