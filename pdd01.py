
def test(n, a):
    a = sorted(a)
    sum_ = 0
    for i in a[n % 3::3]:
        sum_ += i

    print(sum(a) - sum_)


if __name__ == '__main__':
    # n = int(input())
    # a = list(map(int, input().split()))
    test(8, [100,200,300, 400, 500, 600, 700, 800])
    # test(n, a)
    # print(reduce(add, range(1, 5)))
