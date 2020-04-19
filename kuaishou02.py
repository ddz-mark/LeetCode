import sys


def test(n):
    add = [8, 7, -1, 9, -1, 9, 8, -1, -1, 8]
    delnum = [-1, -1, -1, -1, -1, -1, 5, -1, 9, 5]

    j = len(n) - 1
    for i in range(0, len(n)):
        if add[n[i]] == -1:
            continue
        if delnum[n[j]] == -1:
            j -= 1
        if i == j:
            break
        n[i] = add[n[i]]
        n[j] = delnum[n[j]]
        # add[n[i]], delnum[n[j]] = delnum[n[j]], add[n[i]]
        print(int("".join([str(k) for k in n])))
        break


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    n = [int(i) for i in str(n)]
    test(n)
    # print(calbitsum(101))
