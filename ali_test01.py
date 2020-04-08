import sys


def test(T, m, n, a, b):
    
    pass

if __name__ == '__main__':
    # print(test(4, [1,3,7,15]))
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    print(test(n, a))
