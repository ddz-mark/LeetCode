from operator import add
from functools import reduce

from operator import add
from functools import reduce
import operator


def test(n, k, a):
    avg = round(reduce(add, a) / n)
    dic = dict()
    for i, v in enumerate(a):
        if avg == v:
            k -= 1
            continue
        else:
            dic[i] = abs(v - avg)
    dic = dict(sorted(dic.items(), key=lambda kv: (kv[1], -kv[0])))  # 对字典先按值升序，再按值降序
    loss = 0
    for i in list(dic.keys())[0:k]:
        a[i] = avg
        loss += dic[i]
    a = [str(i) for i in a]
    print(loss)
    print("".join(a))


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, str(input())))
    # test(6, 5, [7, 8, 7, 5, 8, 5])
    test(n, k, a)
    # print(reduce(add, range(1, 5)))
    # dic = {"1": 2, "2": 1}
    # print(dict(sorted(dic.items(), key=operator.itemgetter(1))))
